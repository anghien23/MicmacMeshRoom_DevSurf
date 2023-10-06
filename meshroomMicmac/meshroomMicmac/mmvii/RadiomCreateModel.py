__version__ = "2.0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class RadiomCreateModel(node.MicmacNode):
    commandLine = 'MMVII RadiomCreateModel {imageNameValue} {outputRadValue} {inputCalibValue} DegIma={DegImaValue} DegRadSens={DegRadSensValue}'
    documentation = 'RadiomCreateModel'
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
            label='Pattern images names',
            description="Name of image",
            uid=[0],
        group='unnamedParams',
            value='',
        ),
        desc.File(
            name='inputCalib',
            label='input Calibration',
            description="InputCalibration",
            uid=[0],
        group='unnamedParams',
            value='',
        ),
        desc.File(
            name='inputRadModel',
            label='input Radiometric Model',
            description="Input RadModel",
            uid=[0],
        group='unnamedParams',
            value='',
        ),
        desc.StringParam(
            name='XXX',
            label='X X X',
            description="YYY",
            uid=[0],
            value='',
        ),
        desc.IntParam(
            name='DegIma',
            label='Deg Ima',
            description="Degree for per image polynomial",
            uid=[0],
            range=(0,9,1),
            value=0,
        ),
        desc.IntParam(
            name='DegRadSens',
            label='Deg Rad Sens',
            description="Degree for per sens radial model",
            uid=[0],
            range=(0,9,1),
            value=5,

        ),

    ]

    outputs = [
        desc.File(
            name='outputRad',
            label='output Radiometric Model',
            description="Output RadModel",
            uid=[],
        group='unnamedParams',
            value='Init2',
        ),
    ]
