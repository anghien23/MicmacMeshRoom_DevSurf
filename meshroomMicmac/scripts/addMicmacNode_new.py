#!/usr/bin/env python

# MicMac v1.1.1 command-line to Meshroom node
# Custom script written from meshroom_newNodeType

from __future__ import print_function

import argparse
import os
import re
import sys
import shlex
import subprocess
from pprint import pprint
import json

def trim(s):
    """
    All repetition of any kind of space is replaced by a single space
    and remove trailing space at beginning or end.
    """
    # regex to replace all space groups by a single space
    # use split() to remove trailing space at beginning/end
    return re.sub('\s+', ' ', s).strip()


def quotesForStrings(valueStr):
    """
    Return the input string with quotes if it cannot be cast into another builtin type.
    """
    v = valueStr
    try:
        int(valueStr)
    except ValueError:
        try:
            float(valueStr)
        except ValueError:
            if "'" in valueStr:
                v = "'''{}'''".format(valueStr)
            else:
                v = "'{}'".format(valueStr)
    return v

def convertToLabel(name):
    camelCaseToLabel = re.sub('()([A-Z][a-z]*?)', r'\1 \2', name)
    if camelCaseToLabel[0] == ' ': # begin with uppercase
        camelCaseToLabel = camelCaseToLabel[1:]
    snakeToLabel = ' '.join(word.capitalize() for word in camelCaseToLabel.split('_'))
    snakeToLabel = ' '.join(word.capitalize() for word in snakeToLabel.split(' '))
    return snakeToLabel


def compute_args(argName, argType, argDesc, argValue, argRange, outputNodeStr, inputNodeStr, nbUnnamedParams):
    """
    Compute one argument for one command
    """
    cmdLineArgLower = ' '.join([argName, argDesc]).lower()

    # Detect if mandatory arg
    if len(argName) == 0 :
        nbUnnamedParams += 1
        argName = 'unnamed_' + str(nbUnnamedParams)
        isUnnamed = True
    else :
        isUnnamed = False

    # Only mandatory args can be outputs
    if 'out' in cmdLineArgLower :
        isOutput = True
    else :
        isOutput = False

    if argType =='string' and ('path' in cmdLineArgLower or 'folder' in cmdLineArgLower or 'file' in cmdLineArgLower or 'directory' in cmdLineArgLower or 'dir' in cmdLineArgLower) :
        argType='file'

    print([argName, argType, argDesc])

    paramStr="""
            name='{name}',
            label='{label}',
            description="{description}",
            uid=[0],""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    
    if isUnnamed:
        paramStr += """
        group='unnamedParams',"""

    if argType == 'bool':
        argStr="""
        desc.BoolParam({params}
            value={value},
        ),""".format(params=paramStr, value=argValue if argValue else "''")
    elif argType == 'file':
        argStr = """
        desc.StringParam({params}
            value={value},
        ),""".format(params=paramStr, value=argValue if argValue else "''")

    elif argType == 'string':
        argStr = """
        desc.StringParam({params}
            value={value},
        ),""".format(params=paramStr, value=argValue if argValue else "''")
    elif argType == 'int':
        argStr = """
        desc.IntParam({params}
            value={value},
            range={range},
        ),""".format(params=paramStr, value=argValue if argValue else 0,range=argRange if argRange else str((-sys.maxsize, sys.maxsize, 1)))
    elif argType == 'double':
        argStr = """
        desc.FloatParam({params}
            value={value},
            range={range},
        ),""".format(params=paramStr, value=argValue if argValue else 0.0, range=argRange if argRange else (-float('inf'), float('inf'), 0.01))
    ### vector : string / double / int
    elif argType == 'std::vector<string>' or 'std::vector<std::string>':
        argStr = """
        desc.ListAttribute({params}
            elementDesc=desc.StringParam(
                name="{name}Item",
                label="{label} item",
                description="{description}",
                value={value},
                uid=[0],
            ),
        ),""".format(params=paramStr, name=argName, label=convertToLabel(argName), description=argDesc, value=argValue if argValue else "")
    elif argType == 'std::vector<double>':
        argStr = """
        desc.ListAttribute({params}
            elementDesc=desc.FloatParam(
                name="{name}Item",
                label="{label} item",
                description="{description}",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
        ),""".format(params=paramStr, name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == 'std::vector<int>':
        argStr = """
        desc.ListAttribute({params}
            elementDesc=desc.IntParam(
                name="{name}Item",
                label="{label} item",
                description="{description}",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
        ),""".format(params=paramStr, name=argName, label=convertToLabel(argName), description=argDesc)


    elif argType == 'pt2di':
        argStr = """
        desc.GroupAttribute(
            name='{name}',
            label='{label}',
            description="{description}",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.IntParam(
                name="x",
                label="X",
                description="x.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="y",
                label="Y",
                description="y.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
        ]),""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == 'pt3di':
        argStr = """
        desc.GroupAttribute(
            name='{name}',
            label='{label}',
            description="{description}",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.IntParam(
                name="x",
                label="X",
                description="x.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="y",
                label="Y",
                description="y.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="z",
                label="Z",
                description="z.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
        ]),""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == 'pt2dr':
        argStr = """
        desc.GroupAttribute(
            name='{name}',
            label='{label}',
            description="{description}",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
        ]),""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == 'pt3dr':
        argStr = """
        desc.GroupAttribute(
            name='{name}',
            label='{label}',
            description="{description}",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="z",
                label="Z",
                description="z.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
        ]),""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == "typemtdim":
        argStr = """
        desc.ChoiceParam({params}
            value="Aperture",
            values=["Focalmm","Aperture","ModelCam","AdditionalName"],
            uid=[0],
        ),""".format(params=paramStr, description=argDesc)

    else:
        print('New MicMac Node Aborted: unknown type (type: ' + argType + ').')
        sys.exit(-1)

    if isOutput:
        outputNodeStr += argStr
    else:
        inputNodeStr += argStr
    return outputNodeStr, inputNodeStr, nbUnnamedParams

# Import JSON arg
f_json = open('/home/ANghien/Documents/data/noeuds_MMVII/MMVII_argsspec.json')

parser = argparse.ArgumentParser(description='Create a new MicMac Node')
parser.add_argument('--node', metavar='NODE_NAME', type=str,
                    help='New node name')
parser.add_argument('--bin', metavar='CMDLINE', type=str,
                    default=None,
                    help='Input executable')
parser.add_argument('--args', metavar='CMDLINE', type=str,
                    default='',
                    help='Input executable parameters')
parser.add_argument('--output', metavar='DIR', type=str,
                    default=os.path.dirname(__file__),
                    help='Output plugin folder')
parser.add_argument("--force", help="Allows to overwrite the output plugin file.",
                    action="store_true")

args = parser.parse_args()
inputCmdLineDoc = None  
proc = subprocess.Popen(args=shlex.split(args.bin) + [args.args] + ['-help'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
inputCmdLineDoc = stdout if stdout else stderr

if not inputCmdLineDoc:
    print('No input documentation.')
    print('Usage: YOUR_COMMAND -help | {cmd}'.format(cmd=os.path.splitext(__file__)[0]))
    sys.exit(-1)


## Detect args and add them into 
data_json = json.load(f_json)
print('='*80)

outputNodeStr = ''
inputNodeStr = ''
nbUnnamedParams = 0

for command in data_json['applets']:
    if command['name'] == args.node:
        for arg_mandat in command['mandatory']:
            argStr = None
            argName = ''
            argType = arg_mandat['type'].lower()
            argDesc = trim(arg_mandat['comment'])
            argValue = ''
            # If argument range is specified, else
            try:
                argRange = arg_mandat['range'] 
            except:
                argRange = None
            isOutput = False
            isUnnamed = False

            # Add mandatory args in node  
            outputNodeStr, inputNodeStr, nbUnnamedParams = compute_args(argName, argType, argDesc, argValue, argRange, outputNodeStr, inputNodeStr, nbUnnamedParams)
        
        for arg_opt in command['optional']:
            argName = arg_opt['name']
            argType = arg_opt['type'].lower()
            argDesc = trim(arg_opt['comment'])
            # If argument default is specified, else
            try:
                argValue = arg_opt['default'] 
            except:
                argValue=""
            # If argument range is specified, else
            try:
                argRange = arg_opt['range'] 
            except:
                argRange = None
            isOutput = False
            isUnnamed = False

            # Add optionnal args in node
            outputNodeStr, inputNodeStr, nbUnnamedParams = compute_args(argName, argType, argDesc, argValue, argRange, outputNodeStr, inputNodeStr, nbUnnamedParams)

            




outputNodeStr = re.sub('(uid=\[0\])', lambda m: 'uid=[]', outputNodeStr) # remove uid for output parameters

fileStr = '''__version__ = "2.0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class {nodeName}(node.MicmacNode):
    commandLine = '{cmd} {allParams}'
    documentation = '{nodeName}'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group="micmac",
            uid=[0],
        ),{inputNodes}
    ]

    outputs = [{outputNodes}
    ]
'''.format(nodeName=args.node, cmd=args.bin + ' ' + args.args, allParams= '{allParams}', inputNodes=inputNodeStr, outputNodes=outputNodeStr)

outputFilepath = os.path.join(args.output, args.node + '.py')

if not args.force and os.path.exists(outputFilepath):
    print('Plugin "{}" already exists "{}".'.format(args.node, outputFilepath))
    sys.exit(-1)

with open(outputFilepath, 'w') as pluginFile:
    pluginFile.write(fileStr)

print('New node exported to: "{}"'.format(outputFilepath))
