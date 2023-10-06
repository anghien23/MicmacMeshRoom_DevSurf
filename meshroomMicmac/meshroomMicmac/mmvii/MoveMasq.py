__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class MoveMasq(node.MicmacNode):
    commandLine = '/home/ANghien/Documents/Meshroom_x_MicMac/meshroomMicmac/scripts/moveMasq.sh'
    documentation = 'MoveMasq'
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
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description="Full name (Dir+Pat)",
            uid=[0],
        group='unnamedParams',
            value="",
        ),
        desc.File(
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            group='', # unnamed parameter
            value="",
            uid=[0],
        ),
        
    ]

    outputs = [
    	desc.File(
            name='Orientation',
            label='Output Orientation',
            description="Out : orientation",
            uid=[0],
        group='unnamedParams',
            value="Basc",
        ),
    ]
