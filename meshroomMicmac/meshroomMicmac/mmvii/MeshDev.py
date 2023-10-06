__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class MeshDev(node.MicmacNode):
    commandLine = 'MMVII MeshDev {inputMeshValue} {allParams}'
    documentation = 'MeshDev'
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
            name='inputMesh',
            label='Name of input cloud/mesh',
            description="Name of input file",
            uid=[0],
            value="",
            group='unnamedParams',
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description="Generate out in binary format ,[Default=false]",
            uid=[0],
            value=False,
        ),
        desc.IntParam(
            name='NbCByS',
            label='Nb C By S',
            description="Number of compensation by step ,[Default=3]",
            uid=[0],
            value=3,
            range=(0, 10, 1),
        ),
        desc.BoolParam(
            name='ShowAv',
            label='Show Av',
            description="Show advancement of computation ,[Default=true]",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='ErrorUnReached',
            label='Error Un Reached',
            description="Generate error when not connected mesh ,[Default=false]",
            uid=[0],
            value=False,
        ),
        desc.FloatParam(
            name='WDistE',
            label='WDistE',
            description="Weight on edge dist ,[Default=0]",
            uid=[0],
            value=0.0,
            range=(0.0, 5.0, 0.01),
        ),
        desc.FloatParam(
            name='WRot',
            label='WRot',
            description="Weight on rot on 2d triangles ,[Default=1]",
            uid=[0],
            value=1.0,
            range=(0.0, 5.0, 0.01),
        ),

    ]

    outputs = [
        desc.File(
            name='Out',
            label='Name of ouput dev',
            description="Name of output file",
            uid=[],
            value="Dev3D_Clip_Correc_mesh.ply",
        ),
    ]
