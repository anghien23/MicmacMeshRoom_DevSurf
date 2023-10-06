__version__ = "1.0"

from meshroom.core import desc
from meshroomMicmac.custom import node

class Malt(node.MicmacNode):
    commandLine = 'mm3d Malt {correlationModeValue} {imagePatternValue} {orientationValue} NbVI={NbViValue} ZoomF={ZoomFValue} ResolTerrain={ResolTerrainValue} DefCor={DefCorValue} CostTrans={CostTransValue} EZA={EZAValue}'
    documentation = '''Malt'''

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group='', # required to execute mm3d command line
            uid=[0],
        ),
        desc.ChoiceParam(
            name='correlationMode',
            label='Correlation Mode',
            description='Correlation Mode',
            value='Ortho',
            values=["Ortho", "UrbanMNE", "GeomImage"],
            exclusive=True,
            group='', # unnamed parameter
            uid=[0],
        ),   
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            value="",
            group='', # unnamed parameter
            uid=[0],
        ),    
        desc.File(
            name='orientation',
            label='Orientation Directory',
            description='Orientation directory name.',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
        desc.File(
            name='waitFor',
            label='Wait For',
            description='Wait for previous step to be done',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
        desc.IntParam(
            name='NbVi',
            label='Nb Visible Images',
            description='Number of Visible Images required',
            value=3,
            range=(2, 20, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='ZoomF',
            label='Final Zoom',
            description='Final Zoom',
            value=2,
            range=(1, 20, 1),
            uid=[0],
        ),
        desc.FloatParam(
            name='ResolTerrain',
            label='Ground Resolution',
            description='Ground Resolution',
            value=0.5,
            range=(0.1, 5.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='DefCor',
            label='Default Correlation',
            description='Default Correlation in un correlated pixels',
            value=0.2,
            range=(0.1, 1.0, 0.1),
            uid=[0],
        ),
        desc.FloatParam(
            name='CostTrans',
            label='Correlation Cost',
            description='Cost to change from correlation to uncorrelation',
            value=2.0,
            range=(1.0, 10.0, 0.1),
            uid=[0],
        ),
        desc.IntParam(
            name='EZA',
            label='Export Z Absolute',
            description='Export Z Absolute',
            value=1,
            range=(0, 1, 1),
            uid=[0],
        ),
    ]

    outputs = [
    	desc.File(
            name='IsDone',
            label='Is Done',
            description='''Next step must wait''',
            value="",
            group='', # unnamed parameter
            uid=[],
        ),
    ]
