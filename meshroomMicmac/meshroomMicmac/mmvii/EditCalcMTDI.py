__version__ = "2.0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class EditCalcMTDI(node.MicmacNode):
    commandLine = 'MMVII EditCalcMTDI {inputMetaValue} {typeMetaValue} {allParams}'
    documentation = 'EditCalcMTDI'
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
        desc.StringParam(
            name='inputMeta',
            label='Input MetaData',
            description="Input MetaData",
            uid=[0],
            group='unnamedParams',
            value='',
        ),
        desc.StringParam(
            name='typeMeta',
            label='Type of MetaData',
            description="Type of MetaData",
            uid=[0],
            group='unnamedParams',
            value='',
        ),

#        desc.ListAttribute(
#            name='typeMeta',
#            label='Type MetaData',
#            description="Type of meta-data",
#            group='unnamedParams',
#            elementDesc=desc.StringParam(
#                name="unnamed_2Item",
#                label="Unnamed 2 item",
#                description="Type of meta-data",
#                value='',
#                uid=[0],
#            ),
#        ),

        desc.StringParam(
            name='ImTest',
            label='Im Test',
            description="Im for testing rules",
            uid=[0],
            value='',
        ),
        desc.BoolParam(
            name='Show',
            label='Show',
            description="Show all rules",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='Save',
            label='Save',
            description="Save result in a new file",
            uid=[0],
            value=False,
        ),

        desc.StringParam(
            name='Modif',
            label='Modif',
            description="Modification [Pat,Subst,Rank], Rank: {at(0)... ,-1 front,High back,at(0),-2 replace }",
            uid=[0],
            value= '[.*.tif,11,0]',
        ),

    ]

    outputs = [
        desc.StringParam(
            name='OutMetaData',
            label='Out Meta Data',
            description="Output MetaData",
            uid=[],
            value='',
        ),

    ]
