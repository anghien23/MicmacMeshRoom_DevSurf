__version__ = "2.0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class RadiomComputeEqual(node.MicmacNode):
    commandLine = 'MMVII RadiomComputeEqual {imageNameValue} {inputRadDataValue} {inputRadModelValue} {outputRadModelValue} {allParams}'
    documentation = 'RadiomComputeEqual'
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
            name='imageName',
            label='Pattern images name',
            description="Name of image",
            uid=[0],
        group='unnamedParams',
            value='',
        ),
        desc.File(
            name='inputRadData',
            label='input Radiometric Data',
            description="Input RadData",
            uid=[0],
        group='unnamedParams',
            value='',
        ),
        desc.File(
            name='inputRadModel',
            label='input Radiometric Model',
            description="Input RadModel",
            uid=[0],
        group='unnamedParams',
            value='',
        ),
        desc.BoolParam(
            name='Show',
            label='Show',
            description="Show messages",
            uid=[0],
            value=True,
        ),
        desc.FloatParam(
            name='WStabIm',
            label='Weight for stabilization Image Pol/avoid drift (relative tot W)',
            description="Show messages",
            uid=[0],
            value=0.01,
            range=(0.0,1.0, 0.01),
        ),
        desc.FloatParam(
            name='WFixCste',
            label='Weight for fixing constant',
            description="Weight for fixing constant",
            uid=[0],
            value=0.0,
            range=(0.0,1.0,0.01),
        ),
        desc.IntParam(
            name='NbIter',
            label='Number of Iteration',
            description="Number iter/step",
            uid=[0],
            value=2,
            range=(0,5,1),
        ),

    ]

    outputs = [
        desc.File(
            name='outputRadModel',
            label='output Radiometric Model',
            description="Output RadModel",
            uid=[],
        group='unnamedParams',
            value='Equal',
        ),
    ]
