{
    "header": {
        "pipelineVersion": "2.2",
        "releaseVersion": "2023.3.0-develop",
        "fileVersion": "1.1",
        "template": false,
        "nodesVersions": {
            "SaisieMasq": "1.1.1",
            "RadiomCreateModel": "2.0.0",
            "MeshCheck": "0.0",
            "TapiocaMulScale": "1.1.1",
            "SBGlobBascule": "1.1.1",
            "MeshImageDevlp": "2.0.0",
            "RadiomComputeEqual": "2.0.0",
            "SaisieMasqQT": "1.1.1",
            "TiPunch": "1.1.1",
            "MeshDev": "1.1.1",
            "MicMacProject": "1.0",
            "C3DC": "1.1.1",
            "MeshProjImage": "2.0.0",
            "OriConvV1V2": "1.1.1",
            "MeshCloudClip": "1.1.1",
            "SubSample": "1.1.1",
            "AperiCloud": "1.1.1",
            "EditCalcMTDI": "2.0.0",
            "Tapas": "1.1.1",
            "CameraInit": "9.0",
            "SaisieBasc": "0.0"
        }
    },
    "graph": {
        "CameraInit_1": {
            "nodeType": "CameraInit",
            "position": [
                -929,
                -182
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 0,
                "split": 1
            },
            "uids": {
                "0": "961e54591174ec5a2457c66da8eadc0cb03d89ba"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "viewpoints": [],
                "intrinsics": [],
                "sensorDatabase": "${ALICEVISION_SENSOR_DB}",
                "lensCorrectionProfileInfo": "${ALICEVISION_LENS_PROFILE_INFO}",
                "lensCorrectionProfileSearchIgnoreCameraModel": true,
                "defaultFieldOfView": 45.0,
                "groupCameraFallback": "folder",
                "allowedCameraModels": [
                    "pinhole",
                    "radial1",
                    "radial3",
                    "brown",
                    "fisheye4",
                    "fisheye1",
                    "3deanamorphic4",
                    "3deradial4",
                    "3declassicld"
                ],
                "rawColorInterpretation": "LibRawWhiteBalancing",
                "colorProfileDatabase": "${ALICEVISION_COLOR_PROFILE_DB}",
                "errorOnMissingColorProfile": true,
                "viewIdMethod": "metadata",
                "viewIdRegex": ".*?(\\d+)",
                "verboseLevel": "info"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "output": "{cache}/{nodeType}/{uid0}/cameraInit.sfm"
            }
        },
        "MicMacProject_1": {
            "nodeType": "MicMacProject",
            "position": [
                -687,
                -160
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "f054c6e152a6b9263adbbebba547907418b2199f"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "input": "{CameraInit_1.output}",
                "verboseLevel": "info"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "projectDirectory": "{cache}/{nodeType}/{uid0}/project"
            }
        },
        "TiPunch_1": {
            "nodeType": "TiPunch",
            "position": [
                1142,
                -240
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "658a16659737005c2fe3453947f2233440ec2846"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{C3DC_1.projectDirectory}",
                "Pattern": "{C3DC_1.imagePattern}",
                "plyName": "{C3DC_1.pointCloud}",
                "Bin": true,
                "Depth": 8,
                "Rm": true,
                "Filter": false,
                "Mode": "{C3DC_1.mode}",
                "Scale": 2,
                "FFB": true
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "Out": "TiPunch.ply"
            }
        },
        "MeshProjImage_1": {
            "nodeType": "MeshProjImage",
            "position": [
                1981,
                -256
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "91d45497cec68f5bb0cfb971dd579c07b491a571"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{EditCalcMTDI_1.projectDirectory}",
                "imageName": "{TiPunch_1.Pattern}",
                "inputCloud": "{MeshDev_1.Out}",
                "inputOri": "{OriConvV1V2_1.Ori}"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "outputMeshDev": "DEV",
                "OutRadData": "R0"
            }
        },
        "EditCalcMTDI_1": {
            "nodeType": "EditCalcMTDI",
            "position": [
                1763,
                -69
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "a3d0fd00d2dfc5706406d03d5bf991322957a071"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{OriConvV1V2_1.projectDirectory}",
                "inputMeta": "Std",
                "typeMeta": "Aperture",
                "ImTest": "",
                "Show": false,
                "Save": true,
                "Modif": "[.*.tif,11,0]"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "OutMetaData": ""
            }
        },
        "RadiomCreateModel_1": {
            "nodeType": "RadiomCreateModel",
            "position": [
                2202,
                -167
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "72573be1462c694199ee8be5f1e369075c26531b"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{MeshProjImage_1.projectDirectory}",
                "imageName": "{MeshProjImage_1.imageName}",
                "inputCalib": "{MeshProjImage_1.inputOri}",
                "XXX": "",
                "DegIma": 2,
                "DegRadSens": 5
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "outputRad": "Init2"
            }
        },
        "RadiomComputeEqual_1": {
            "nodeType": "RadiomComputeEqual",
            "position": [
                2407,
                -247
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "f8528333ec6388ec4a1fd8654c87b206dff1b3d6"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{RadiomCreateModel_1.projectDirectory}",
                "imageName": "{RadiomCreateModel_1.imageName}",
                "inputRadData": "{MeshProjImage_1.OutRadData}",
                "inputRadModel": "{RadiomCreateModel_1.outputRad}",
                "Show": true,
                "WStabIm": 0.01,
                "WFixCste": 0.0,
                "NbIter": 2
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "outputRadModel": "Equal"
            }
        },
        "MeshImageDevlp_1": {
            "nodeType": "MeshImageDevlp",
            "position": [
                2643,
                -154
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "ab4537650e73981b3b08c7bab5dff09da96d4a21"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{RadiomComputeEqual_1.projectDirectory}",
                "NameDevlpMesh": "Dev2D_Clip_Correc_mesh.ply",
                "inputMesh": "{MeshProjImage_1.outputMeshDev}",
                "WGL": false,
                "WRGBL": false,
                "InRadModel": "{RadiomComputeEqual_1.outputRadModel}",
                "WithNormal": false
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {}
        },
        "AperiCloud_1": {
            "nodeType": "AperiCloud",
            "position": [
                540,
                -168
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "4771ad5c8cbac88fa76695fb0e78ea67fdb210fe"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{SBGlobBascule_1.projectDirectory}",
                "imagePattern": "{SBGlobBascule_1.imagePattern}",
                "orientationDir": "{SBGlobBascule_1.Orientation}",
                "ExpTxt": false,
                "Bin": true,
                "RGB": true,
                "WithPoints": true,
                "WithCam": true,
                "SeuilEc": 10.0,
                "LimBsH": 0.01,
                "CalPerIm": false,
                "StepIm": -1.0,
                "ProfCam": 0.3,
                "RabDrBundle": 0.0,
                "SavePtsCol": true,
                "GCPCtrl": [],
                "Out": "AperiCloud.ply"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "pointCloud": "{OutValue}"
            }
        },
        "C3DC_1": {
            "nodeType": "C3DC",
            "position": [
                924,
                -160
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "437a92e1815a148c3914740d9b2c6e64371faf6d"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{SaisieMasqQT_1.projectDirectory}",
                "imagePattern": "{SaisieMasqQT_1.imagePattern}",
                "orientationDir": "{SaisieMasqQT_1.orientationDir}",
                "mode": "BigMac",
                "Masq3D": "{SaisieMasqQT_1.Output Masq}",
                "SzNorm": 2,
                "PlyCoul": true,
                "Purge": true,
                "ExpTxt": false,
                "Bin": true,
                "NormByC": false,
                "TetaOpt": 0.17,
                "ExpImSec": true,
                "setCustomZoomF": false,
                "ZoomF": 2,
                "FilePair": "",
                "OffsetPly": {
                    "x": 0.0,
                    "y": 0.0,
                    "z": 0.0
                },
                "Out": "C3DC.ply"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "pointCloud": "{OutValue}"
            }
        },
        "Tapas_1": {
            "nodeType": "Tapas",
            "position": [
                -237,
                -164
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "21b66c0ac60b24bef617894f6c3ce83afbcebbb5"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{TapiocaMulScale_1.projectDirectory}",
                "imagePattern": "{TapiocaMulScale_1.imagePattern}",
                "calibrationModel": "FraserBasic",
                "PostFix": "{TapiocaMulScale_1.PostFix}",
                "InCal": "",
                "InOri": "",
                "ExpTxt": false,
                "FrozenPoses": "",
                "FrozenCalibs": "",
                "RefineAll": true,
                "ImInit": "",
                "EcInit": {
                    "max": 100.0,
                    "min": 5.0
                },
                "EcMax": 5.0,
                "setLibPP": false,
                "LibPP": true,
                "setLibFoc": false,
                "LibFoc": true,
                "setLibCP": false,
                "LibCP": true,
                "setLibCD": false,
                "LibCD": true,
                "setLibDec": false,
                "LibDec": true,
                "setDegRadMax": false,
                "DegRadMax": 0,
                "setDRMax": false,
                "DRMax": 0,
                "PropDiag": 1.0,
                "setVitesseInit": false,
                "VitesseInit": 2,
                "FocFree": true,
                "PPFree": true,
                "AffineFree": true,
                "BlocGlob": [],
                "DistBlocGlob": [],
                "BlocTimeRel": [],
                "OptBlocG": [],
                "RegulDist": [],
                "Out": "Relative"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "orientationDirectory": "{OutValue}"
            }
        },
        "TapiocaMulScale_1": {
            "nodeType": "TapiocaMulScale",
            "position": [
                -444,
                -153
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "a01e6ea3abb7d250768461598c0c628e1a3ae7ee"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "/home/ANghien/Documents/data/test_micmac_meshroom/jeux_brut",
                "imagePattern": "\"seine-1400[0-1][9,3,4][0-1].tif\"",
                "Pat2": "",
                "imageSizeLowResolution": 400,
                "imageSizeHighResolution": 1500,
                "setByP": false,
                "ByP": -1,
                "NbMinPt": 2,
                "ExpTxt": false,
                "NoMax": false,
                "NoMin": false,
                "Ratio": 0.6,
                "wallisFilter": "@SFS"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "PostFix": ""
            }
        },
        "MeshDev_1": {
            "nodeType": "MeshDev",
            "position": [
                1757,
                -293
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "1a9eb23a0001740bde6dc8e8c15b83d22e1bfbf3"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{MeshCloudClip_1.projectDirectory}",
                "inputMesh": "{MeshCloudClip_1.Out}",
                "Bin": false,
                "NbCByS": 3,
                "ShowAv": false,
                "ErrorUnReached": false,
                "WDistE": 0.0,
                "WRot": 1.0
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "Out": "Dev3D_Clip_Correc_mesh.ply"
            }
        },
        "SaisieMasqQT_1": {
            "nodeType": "SaisieMasqQT",
            "position": [
                730,
                -161
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "439f69b97c59919e3251710f4a9eab950b994a48"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{AperiCloud_1.projectDirectory}",
                "filePath": "{AperiCloud_1.pointCloud}",
                "Attr": "Plan",
                "imagePattern": "{AperiCloud_1.imagePattern}",
                "orientationDir": "{AperiCloud_1.orientationDir}"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "Output Masq": "AperiCloud_selectionInfo.xml"
            }
        },
        "MeshCheck_1": {
            "nodeType": "MeshCheck",
            "position": [
                1348,
                -296
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "124a5316b4931e84e7e77d72ddc15ba11c7336ad"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{TiPunch_1.projectDirectory}",
                "Cloud": "{TiPunch_1.Out}",
                "Bin": false,
                "Do2DC": false,
                "Correct": true
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "Out": "Correc_mesh.ply"
            }
        },
        "MeshCloudClip_1": {
            "nodeType": "MeshCloudClip",
            "position": [
                1563,
                -297
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "39e0b803eecf23cee21386d79b7feeb0b0ddc65a"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{MeshCheck_1.projectDirectory}",
                "Cloud": "{MeshCheck_1.Out}",
                "3DReg": "{SaisieMasqQT_2.Output Masq}",
                "Bin": false,
                "NbMinV": 3
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "Out": "Clip_Correc_mesh.ply"
            }
        },
        "OriConvV1V2_1": {
            "nodeType": "OriConvV1V2",
            "position": [
                1378,
                -32
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "a7c1cfdc0e360f49f5144b37b411ddc62ec73867"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{MeshDev_1.projectDirectory}",
                "In": "{C3DC_1.orientationDir}"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "Ori": "OriV2"
            }
        },
        "SBGlobBascule_1": {
            "nodeType": "SBGlobBascule",
            "position": [
                355,
                -171
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "58c823e207826349a6832dfec54c75c886ce1fe9"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{SaisieMasq_1.projectDirectory}",
                "imagePattern": "{SaisieMasq_1.imagePattern}",
                "orientationDir": "{SaisieMasq_1.orientationDir}",
                "xmlMeasures": "{SaisieMasq_1.xmlMeasures}",
                "PostPlan": "Plan",
                "DistFS": 10.0,
                "Rep": "",
                "CPI": false
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "Orientation": "Basc"
            }
        },
        "SaisieBasc_1": {
            "nodeType": "SaisieBasc",
            "position": [
                -29,
                -164
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "1344bc892115bf7860ff8099d5f7fe5ebea7db78"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imageName": "A_REMPLIR",
                "Orientation": "{Tapas_1.orientationDirectory}",
                "SzW": {
                    "x": 500,
                    "y": 500
                },
                "ForceGray": true,
                "imagePattern": "{Tapas_1.imagePattern}"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "Output": "MesBasc.xml"
            }
        },
        "SaisieMasq_1": {
            "nodeType": "SaisieMasq",
            "position": [
                167,
                -157
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "aaf78e901884d921f473119a9fa871b4fb721496"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{SaisieBasc_1.projectDirectory}",
                "imagePath": "{SaisieBasc_1.Output}",
                "Attr": "Plan",
                "imagePattern": "{SaisieBasc_1.imagePattern}",
                "orientationDir": "{SaisieBasc_1.Orientation}"
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "xmlMeasures": "MesBasc.xml"
            }
        },
        "SubSample_1": {
            "nodeType": "SubSample",
            "position": [
                1143,
                -350
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "5accc71c31816d77e453fcded8aab05ed31aab9f"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{C3DC_1.projectDirectory}",
                "InpointCloud": "{C3DC_1.pointCloud}",
                "Dist": 0.1
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "OutpointCloud": "AperiCloud.ply"
            }
        },
        "SaisieMasqQT_2": {
            "nodeType": "SaisieMasqQT",
            "position": [
                1345,
                -434
            ],
            "parallelization": {
                "blockSize": 0,
                "size": 1,
                "split": 1
            },
            "uids": {
                "0": "a2073a997e82c917d51797248fac5814473b8edd"
            },
            "internalFolder": "{cache}/{nodeType}/{uid0}/",
            "inputs": {
                "projectDirectory": "{SubSample_1.projectDirectory}",
                "filePath": "{SubSample_1.OutpointCloud}",
                "Attr": "",
                "imagePattern": "",
                "orientationDir": ""
            },
            "internalInputs": {
                "invalidation": "",
                "comment": "",
                "label": "",
                "color": ""
            },
            "outputs": {
                "Output Masq": "AperiCloud_selectionInfo.xml"
            }
        }
    }
}