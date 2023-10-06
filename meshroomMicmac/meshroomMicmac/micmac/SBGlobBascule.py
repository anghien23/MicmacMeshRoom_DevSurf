__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class SBGlobBascule(node.MicmacNode):
    commandLine = 'mm3d SBGlobBascule {imagePatternValue} {orientationDirValue} MesBasc-S2D.xml {OrientationValue}  PostPlan={PostPlanValue} DistFS={DistFSValue}'
    documentation = 'SBGlobBascule'

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
            description="Orientation in",
            uid=[0],
        group='unnamedParams',
            value="",
        ),
        desc.File(
            name='xmlMeasures',
            label='XML measures file',
            description="Images measures xml file",
            uid=[0],
        group='unnamedParams',
            value="",
        ),
        desc.StringParam(
            name='PostPlan',
            label='Post Plan',
            description="Set NONE if no plane",
            uid=[0],
            value="Plan",
        ),
        desc.FloatParam(
            name='DistFS',
            label='Dist F S',
            description="Distance between Ech1 and Ech2 to fix scale (if not given no scaling)",
            uid=[0],
            value=10.0,
            range=(0.0, float('inf'), 0.01),
        ),
        desc.StringParam(
            name='Rep',
            label='Rep',
            description="Target coordinate system (Def = ki, ie normal is vertical)",
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='CPI',
            label='C P I',
            description="Calibration Per Image (Def=false)",
            uid=[0],
            value=False,
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
