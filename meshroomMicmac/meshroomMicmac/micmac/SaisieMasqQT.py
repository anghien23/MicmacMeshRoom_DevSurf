__version__ = "0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class SaisieMasqQT(node.MicmacNode):
    commandLine = 'mm3d SaisieMasqQT {filePathValue}'
    documentation = 'SaisieMasqQT'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group="micmac",
            uid=[0],
        ),
        desc.File(
            name='filePath',
            label='File Path',
            description='''Path of the file to open (image or PLY or camera XML).''',
            group='', # unnamed parameter
            value="",
            uid=[0],
        ),
        desc.StringParam(
            name='Attr',
            label='Attr',
            description='''Output file postfix.''',
            value="",
            uid=[0],
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            value="",
            group='', # unnamed parameter
            uid=[0],
        ),    
        desc.File(
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
        desc.File(
            name='waitFor',
            label='Wait For',
            description='Wait for previous step to be done',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
    ]

    outputs = [
    	desc.File(
            name='OutputMasq',
            label='Output Masq',
            description="Name of output masq",
            uid=[],
            value="AperiCloud_selectionInfo.xml",
        ),
    ]
