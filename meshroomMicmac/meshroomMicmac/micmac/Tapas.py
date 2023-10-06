__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class Tapas(node.MicmacNode):
    commandLine = 'mm3d Tapas {calibrationModelValue} {imagePatternValue} {allParams}'
    documentation = 'Tapas'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group='', # required to execute mm3d command line
            uid=[0],
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            group='', # unnamed parameter
            value="",
            uid=[0],
        ),
        desc.ChoiceParam(
            name='calibrationModel',
            label='Calibration Model',
            description='Calibration model.',
            group='', # unnamed parameter
            value='RadialBasic',
            values=['RadialBasic', 'RadialExtended', 'Fraser', 'FishEyeEqui', 'AutoCal', 'Figee', 'HemiEqui', 'RadialStd', 'FraserBasic', 'FishEyeBasic', 'FE_EquiSolBasic', 'Four7x2', 'Four11x2', 'Four15x2', 'Four19x2', 'AddFour7x2', 'AddFour11x2', 'AddFour15x2', 'Four19x2', 'AddPolyDeg0', 'AddPolyDeg1', 'AddPolyDeg2', 'AddPolyDeg3', 'AddPolyDeg4', 'AddPolyDeg5', 'AddPolyDeg6', 'AddPolyDeg7', 'Ebner', 'Brown', 'FishEyeStereo'],
            exclusive=True,
            uid=[0],
        ),
        desc.File(
            name='PostFix',
            label='Homol Directory', # Directory Postfix
            description='Homol Directory.',
            value="",
            uid=[],
        ),
        desc.File(
            name='InCal',
            label='In Calibration Directory',
            description="Directory of Input Internal Orientation (Calibration)",
            uid=[0],
            value="",
        ),
        desc.File(
            name='InOri',
            label='In Orientation Directory',
            description="Directory of Input External Orientation",
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Tie Points In Txt',
            description="Export in text format.",
            uid=[0],
            value=False,
        ),
        desc.StringParam(
            name='FrozenPoses',
            label='Frozen Poses',
            description="List of frozen external calibration (pattern)",
            uid=[0],
            value="",
            advanced=True,
        ),
        desc.StringParam(
            name='FrozenCalibs',
            label='Frozen Calibrations',
            description="List of frozen internal calibration (pattern)",
            uid=[0],
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='RefineAll',
            label='Refine All',
            description="More refinement at all step, safer and more accurate, but slower",
            uid=[0],
            value=True,
        ),
        desc.StringParam(
            name='ImInit',
            label='Initial Image',
            description="Force first image",
            uid=[0],
            value="",
            advanced=True,
        ),
        desc.GroupAttribute(
            name='EcInit',
            label='Ec Init',
            description="Inital threshold for residual",
            brackets='[]',
            joinChar=',',
            advanced=True,
            groupDesc=[
            desc.FloatParam(
                name="max",
                label="Max",
                description="max.",
                value=100.0,
                range=(0.0, 10000.0, 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="min",
                label="Min",
                description="min.",
                value=5.0,
                range=(0.0, 10000.0, 0.01),
                uid=[0],
            ),
        ]),
        desc.FloatParam(
            name='EcMax',
            label='Maximal Reprojection Error',
            description="Final threshold for residual",
            uid=[0],
            value=5.0,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setLibPP',
            label='Set Lib PP',
            description="Set lib PP.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.BoolParam(
            name='LibPP',
            label='Lib PP',
            description="Free principal point",
            enabled=lambda node: node.setLibPP.value,
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setLibFoc',
            label='Set Lib Foc',
            description="Set lib Foc.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.BoolParam(
            name='LibFoc',
            label='Lib Foc',
            description="Free focal",
            enabled=lambda node: node.setLibFoc.value,
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setLibCP',
            label='Set Lib CP',
            description="Set lib CP.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.BoolParam(
            name='LibCP',
            label='Lib CP',
            description="Free distorsion center, Def context dependant",
            enabled=lambda node: node.setLibCP.value,
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setLibCD',
            label='Set Lib CD',
            description="Set lib CD.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.BoolParam(
            name='LibCD',
            label='Lib CD',
            description="Free distorsion center, Def context dependant. Principal Point should be also free if CD is free",
            enabled=lambda node: node.setLibCD.value,
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setLibDec',
            label='Set Lib Dec',
            description="Set lib Dec.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.BoolParam(
            name='LibDec',
            label='Lib Dec',
            description="Free decentric parameter, Def context dependant",
            enabled=lambda node: node.setLibDec.value,
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setDegRadMax',
            label='Set DegRadMax',
            description="Set DegRadMax.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.IntParam(
            name='DegRadMax',
            label='Deg Rad Max',
            description="Max degree of radial, default model dependent",
            enabled=lambda node: node.setDegRadMax.value,
            uid=[0],
            value=0,
            range=(0, 10, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setDRMax',
            label='Set DR Max',
            description="Set DR Max.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.IntParam(
            name='DRMax',
            label='DR Max',
            description="When specified degree of freedom of radial parameters",
            enabled=lambda node: node.setDRMax.value,
            uid=[0],
            value=0,
            range=(0, 9, 1),
            advanced=True,
        ),
        desc.FloatParam(
            name='PropDiag',
            label='Prop Diag',
            description="Hemi-spherik fisheye diameter to diagonal ratio",
            uid=[0],
            value=1.0,
            range=(0.0, 1.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setVitesseInit',
            label='Set Vitesse Init',
            description="Set vitesse init.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.IntParam(
            name='VitesseInit',
            label='Vitesse Init',
            description="Vitesse Init.",
            enabled=lambda node: node.setVitesseInit.value,
            uid=[0],
            value=2,
            range=(0, sys.maxsize, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='FocFree',
            label='Foc Free',
            description="Foc Free.",
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='PPFree',
            label='PP Free',
            description="Principal Point Free.",
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='AffineFree',
            label='Affine Free',
            description="Affine Parameter.",
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.ListAttribute(
            name='BlocGlob',
            label='Bloc Glob',
            description="Param for Glob bloc compute [File,SigmaCenter,SigmaRot,?MulFinal,?Export].", 
            advanced=True,
            elementDesc=desc.StringParam(
                name="Item",
                label="Item",
                description="item.",
                value="",
                uid=[0],
            ),
        ),
        desc.ListAttribute(
            name='DistBlocGlob',
            label='Dist Bloc Glob',
            description="Param for Dist Glob bloc compute [File,SigmaDist,?MulFinal,?Export].", 
            advanced=True,
            elementDesc=desc.StringParam(
                name="Item",
                label="Item",
                description="item.",
                value="",
                uid=[0],
            ),
        ),
        desc.ListAttribute(
            name='BlocTimeRel',
            label='Bloc Time Rel',
            description="Param for Time Reliative bloc compute [File,SigmaCenter,SigmaRot,?MulFinal,?Export].", 
            advanced=True,
            elementDesc=desc.StringParam(
                name="Item",
                label="Item",
                description="item.",
                value="",
                uid=[0],
            ),
        ),
        desc.ListAttribute(
            name='OptBlocG',
            label='Opt Bloc G',
            description="[SigmaTr,SigmaRot].", 
            advanced=True,
            elementDesc=desc.StringParam(
                name="Item",
                label="Item",
                description="item.",
                value="",
                uid=[0],
            ),
        ),
        desc.ListAttribute(
            name='RegulDist',
            label='Regul Dist',
            description="Parameter fo RegulDist [Val,Grad,Hessian,NbCase,SeuilNb].", 
            advanced=True,
            elementDesc=desc.FloatParam(
                name="Item",
                label="Item",
                description="item.",
                value=1.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
        ),
        desc.StringParam(
            name='Out',
            label='Output Name',
            description="Directory of Output Orientation",
            value="Tapas",
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='orientationDirectory',
            label='Orientation Directory',
            description="Directory of Output Orientation",
            value="{OutValue}",
            group='', # not a command line parameter
            uid=[],
        ),
    ]