__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class SaisieMasq(node.MicmacNode):
    commandLine = 'mm3d SaisieMasqQT IMAGE_POUR_PLAN Attr={AttrValue}'
    documentation = 'SaisieMasq'

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
            name='imagePath',
            label='File Path',
            description='''Path of the file to open (image or PLY or camera XML).''',
            group='', # unnamed parameter
            value="INSERER IMAGE POUR DEFINIR LE PLAN",
            uid=[0],
        ),
        desc.StringParam(
            name='Attr',
            label='Attr',
            description='''Output file postfix.''',
            value="Plan",
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
            name='xmlMeasures',
            label='XML measures file',
            description="Images measures xml file",
            uid=[0],
        group='unnamedParams',
            value="MesBasc.xml",
        ),

    ]
