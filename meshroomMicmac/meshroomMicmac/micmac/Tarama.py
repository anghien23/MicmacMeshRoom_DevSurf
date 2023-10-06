__version__ = "0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class Tarama(node.MicmacNode):
    commandLine = 'mm3d Tarama {imagePatternValue} {orientationValue}'
    documentation = 'Tarama'

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
            name='imagePattern',
            label='Image Pattern',
            description="Full Image (Dir+Pat)",
            uid=[0],
        group='unnamedParams',
            value="",
        ),
        desc.File(
            name='orientation',
            label='Orientation',
            description="Orientation",
            uid=[0],
        group='unnamedParams',
            value="",
        ),
        
    ]

    outputs = [
        desc.File(
            name='outputDirectory',
            label='Output Directory',
            description="Directory for output (Deg=TA)",
            uid=[0],
            value="TA",
        ),
    ]
