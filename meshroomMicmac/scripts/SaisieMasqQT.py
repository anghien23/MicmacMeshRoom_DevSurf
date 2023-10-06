__version__ = "0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class SaisieMasqQT(node.MicmacNode):
    commandLine = 'mm3d SaisieMasqQT {allParams}'
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
    ]

    outputs = [
    ]
