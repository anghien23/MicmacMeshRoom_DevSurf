__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class SubSample(node.MicmacNode):
    commandLine = 'CloudCompare -C_EXPORT_FMT PLY -AUTO_SAVE OFF -O {InpointCloudValue} -SS Spatial {DistValue} -SAVE_CLOUDS FILE "{OutpointCloudValue}"'
    documentation = 'Subsample C3DC point cloud'
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
            name='InpointCloud',
            label='Dense Point Cloud',
            description='Output PLY point cloud name.',
            value='C3DC.ply',
            group='', 
            uid=[0],
        ),
	desc.FloatParam(
            name="Dist",
            label="Mini Distance",
            description="Minimum distance between two points.",
            value=0.1,
            range=(0.0, 10.0, 0.01),
            uid=[0],
        ),

    ]

    outputs = [
        desc.File(
            name='OutpointCloud',
            label='Subsampled Point Cloud',
            description='Output PLY point cloud name.',
            value='AperiCloud.ply',
            group='', # not a command line parameter
            uid=[],
        ),

    ]
