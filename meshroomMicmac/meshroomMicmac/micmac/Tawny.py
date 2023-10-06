__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class Tawny(node.MicmacNode):
    commandLine = 'mm3d Tawny {orthoDirectoryValue} Out={OutValue}'
    documentation = 'Tawny'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group='', # required to execute mm3d command line
            uid=[0],
        ),
        desc.File(
            name='orthoDirectory',
            label='Ortho Directory',
            description="Ortho directory",
            group='', # unnamed parameter
            uid=[0],
            value="",
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
            name='Out',
            label='Orthophoto',
            description="Name of output file (in the folder)",
            uid=[],
            value="Orthophotomosaic.tif",
        ),
    ]
