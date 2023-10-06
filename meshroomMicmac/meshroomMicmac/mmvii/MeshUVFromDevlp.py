__version__ = "2.0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class MeshUVFromDevlp(node.MicmacNode):
    commandLine = 'MMVII MeshUVFromDevlp {allParams}'
    documentation = 'MeshUVFromDevlp'
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
    ]

    outputs = [
    ]
