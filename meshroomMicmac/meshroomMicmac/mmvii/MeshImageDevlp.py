__version__ = "2.0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class MeshImageDevlp(node.MicmacNode):
    commandLine = 'MMVII MeshImageDevlp {NameDevlpMeshValue} {inputMeshValue} {allParams}'
    documentation = 'MeshImageDevlp'
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
            name='NameDevlpMesh',
            label='Name of developed mesh',
            description="Name of 2d devloped mesh",
            uid=[0],
        group='unnamedParams',
            value='Dev2D_Clip_Correc_mesh.ply',
        ),
        desc.File(
            name='inputMesh',
            label='input mesh',
            description="Input MeshDev",
            uid=[0],
        group='unnamedParams',
            value='',
        ),
        desc.BoolParam(
            name='WGL',
            label='WGL',
            description="With Gray Label 2-byte image generation",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='WRGBL',
            label='WRGBL',
            description="With RGB Label 1 chanel-label/2 label contrast",
            uid=[0],
            value=False,
        ),
        desc.File(
            name='InRadModel',
            label='Input Radiometric Model',
            description="Input RadModel",
            uid=[0],
            value='Equal',
        ),
        desc.BoolParam(
            name='WithNormal',
            label='Result With Normal',
            description="Do we want to create images of normals ?",
            uid=[0],
            value=False,
        ),

    ]

    outputs = [

    ]
