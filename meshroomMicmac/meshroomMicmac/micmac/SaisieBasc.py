__version__ = "0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class SaisieBasc(node.MicmacNode):
    commandLine = 'mm3d vSaisieBasc {imageNameValue} {OrientationValue} {OutputValue}'
    documentation = 'SaisieBasc'

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
            label='Image Pattern for Bascule',
            description="Full Name (Dir+Pattern)",
            uid=[0],
        group='unnamedParams',
            value="",
        ),
        desc.File(
            name='Orientation',
            label='Orientation Directory',
            description="Orientation, NONE if unused",
            uid=[0],
        group='unnamedParams',
            value="",
        ),
        desc.GroupAttribute(
            name='SzW',
            label='SzW',
            description="Total size of windows",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.IntParam(
                name="x",
                label="X",
                description="x.",
                value=750,
                range=(100, 2000, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="y",
                label="Y",
                description="y.",
                value=750,
                range=(100, 2000, 1),
                uid=[0],
            ),
        ]),
        desc.BoolParam(
            name='ForceGray',
            label='Force Gray',
            description="Force gray image, def =true",
            uid=[0],
            value=True,
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            value="",
            group='', # unnamed parameter
            uid=[0],
        ),    

    ]

    outputs = [
        desc.File(
            name='Output',
            label='Output file',
            description="Output File",
            uid=[0],
        group='unnamedParams',
            value="MesBasc.xml",
        ),
    ]
