__version__ = "2.0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class EditSet(node.MicmacNode):
    commandLine = 'MMVII EditSet {XmlValue} {OperatorValue} {PatternValue}'
    documentation = 'Create file for images pattern'
    category = 'MicMacV2'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group="micmac",
            uid=[0],
        ),
        desc.ChoiceParam(
            name="Operator",
            label="Operator",
            description="Operator",
            group='', # unnamed parameter
            value="+=",
            values=["+=", "-=", "=", "*=", "=0"],
            exclusive=True,
            uid=[0],
        ),
        desc.StringParam(
            name='Pattern',
            label='Pattern',
            description="Pattern or Xml for modifying",
            uid=[0],
        group='unnamedParams',
            value='.*tif',
        ),

    ]

    outputs = [
        desc.File(
            name='Xml',
            label='Xml File',
            description="Full Name of Xml in/out",
            uid=[],
        group='unnamedParams',
            value='Files.xml',
        ),


    ]
