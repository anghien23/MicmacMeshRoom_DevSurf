__version__ = "2.0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class MeshProjImage(node.MicmacNode):
    commandLine = 'MMVII MeshProjImage {imageNameValue} {inputCloudValue} {inputOriValue} {outputMeshDevValue} {allParams}'
    documentation = 'MeshProjImage'
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
            label='image pattern',
            description="Name of image",
            uid=[0],
            value='',
        group='unnamedParams',
        ),
        desc.File(
            name='inputCloud',
            label='input Cloud',
            description="Name of input cloud/mesh",
            value='Dev3D_Clip_Correc_mesh.ply',
            uid=[0],
        group='unnamedParams',
        ),
        desc.File(
            name='inputOri',
            label='input Ori',
            description="Input Ori",
            uid=[0],
            value='',
        group='unnamedParams',
        ), 
        
        
    ]

    outputs = [
        desc.File(
            name='outputMeshDev',
            label='output Mesh',
            description="Output MeshDev",
            uid=[],
            group='unnamedParams',
            value='DEV'
        ),
        desc.File(
            name='OutRadData',
            label='Out Radiometric Data',
            description="Output RadData",
            uid=[],
            value='R0',
        ),
        


    ]
