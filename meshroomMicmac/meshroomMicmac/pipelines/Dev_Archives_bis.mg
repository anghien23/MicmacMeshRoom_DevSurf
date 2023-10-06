{
    "header": {
        "pipelineVersion": "2.2",
        "releaseVersion": "2023.3.0-develop",
        "fileVersion": "1.1",
        "template": true,
        "nodesVersions": {
            "SBGlobBascule": "1.1.1",
            "AperiCloud": "1.1.1",
            "Tapas": "1.1.1",
            "OriConvV1V2": "1.1.1",
            "TapiocaMulScale": "1.1.1",
            "SaisieMasqQT": "1.1.1",
            "TiPunch": "1.1.1",
            "MeshCheck": "0.0",
            "RadiomCreateModel": "2.0.0",
            "MeshDev": "1.1.1",
            "MeshCloudClip": "1.1.1",
            "C3DC": "1.1.1",
            "SubSample": "1.1.1",
            "MeshImageDevlp": "2.0.0",
            "RadiomComputeEqual": "2.0.0",
            "MeshProjImage": "2.0.0",
            "SaisieBasc": "0.0",
            "EditCalcMTDI": "2.0.0",
            "SaisieMasq": "1.1.1"
        }
    },
    "graph": {
        "TiPunch_1": {
            "nodeType": "TiPunch",
            "position": [
                1142,
                -240
            ],
            "inputs": {
                "projectDirectory": "{C3DC_1.projectDirectory}",
                "Pattern": "{C3DC_1.imagePattern}",
                "plyName": "{C3DC_1.pointCloud}",
                "Filter": false
            }
        },
        "MeshProjImage_1": {
            "nodeType": "MeshProjImage",
            "position": [
                1981,
                -256
            ],
            "inputs": {
                "projectDirectory": "{EditCalcMTDI_1.projectDirectory}",
                "imageName": "{TiPunch_1.Pattern}",
                "inputCloud": "{MeshDev_1.Out}",
                "inputOri": "{OriConvV1V2_1.Ori}"
            }
        },
        "EditCalcMTDI_1": {
            "nodeType": "EditCalcMTDI",
            "position": [
                1763,
                -69
            ],
            "inputs": {
                "projectDirectory": "{OriConvV1V2_1.projectDirectory}",
                "inputMeta": "Std",
                "typeMeta": "Aperture",
                "Save": true
            }
        },
        "RadiomComputeEqual_1": {
            "nodeType": "RadiomComputeEqual",
            "position": [
                2407,
                -247
            ],
            "inputs": {
                "projectDirectory": "{RadiomCreateModel_1.projectDirectory}",
                "imageName": "{RadiomCreateModel_1.imageName}",
                "inputRadData": "{MeshProjImage_1.OutRadData}",
                "inputRadModel": "{RadiomCreateModel_1.outputRad}"
            }
        },
        "MeshImageDevlp_1": {
            "nodeType": "MeshImageDevlp",
            "position": [
                2643,
                -154
            ],
            "inputs": {
                "projectDirectory": "{RadiomComputeEqual_1.projectDirectory}",
                "inputMesh": "{MeshProjImage_1.outputMeshDev}",
                "InRadModel": "{RadiomComputeEqual_1.outputRadModel}"
            }
        },
        "AperiCloud_1": {
            "nodeType": "AperiCloud",
            "position": [
                540,
                -168
            ],
            "inputs": {
                "projectDirectory": "{SBGlobBascule_1.projectDirectory}",
                "imagePattern": "{SBGlobBascule_1.imagePattern}",
                "orientationDir": "{SBGlobBascule_1.Orientation}"
            }
        },
        "Tapas_1": {
            "nodeType": "Tapas",
            "position": [
                -260,
                -162
            ],
            "inputs": {
                "projectDirectory": "{TapiocaMulScale_1.projectDirectory}",
                "imagePattern": "{TapiocaMulScale_1.imagePattern}",
                "calibrationModel": "FraserBasic",
                "PostFix": "{TapiocaMulScale_1.PostFix}",
                "Out": "Relative"
            }
        },
        "TapiocaMulScale_1": {
            "nodeType": "TapiocaMulScale",
            "position": [
                -467,
                -151
            ],
            "inputs": {
                "projectDirectory": "ECRIRE_LE_CHEMIN_DU_REPERTOIRE_DES_IMAGES_ICI",
                "imagePattern": ".*[0-9].(jpg|jpeg|JPG|JPEG|png|PNG|tif|tiff|TIF|TIFF)",
                "imageSizeLowResolution": 400,
                "wallisFilter": "@SFS"
            }
        },
        "MeshDev_1": {
            "nodeType": "MeshDev",
            "position": [
                1757,
                -293
            ],
            "inputs": {
                "projectDirectory": "{MeshCloudClip_1.projectDirectory}",
                "inputMesh": "{MeshCloudClip_1.Out}",
                "ShowAv": false
            }
        },
        "SubSample_1": {
            "nodeType": "SubSample",
            "position": [
                1143,
                -350
            ],
            "inputs": {
                "projectDirectory": "{C3DC_1.projectDirectory}",
                "InpointCloud": "{C3DC_1.pointCloud}"
            }
        },
        "SBGlobBascule_1": {
            "nodeType": "SBGlobBascule",
            "position": [
                332,
                -169
            ],
            "inputs": {
                "projectDirectory": "{SaisieMasq_1.projectDirectory}",
                "imagePattern": "{SaisieMasq_1.imagePattern}",
                "orientationDir": "{SaisieMasq_1.orientationDir}",
                "xmlMeasures": "{SaisieMasq_1.xmlMeasures}"
            }
        },
        "SaisieBasc_1": {
            "nodeType": "SaisieBasc",
            "position": [
                -52,
                -162
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imageName": "A_REMPLIR",
                "Orientation": "{Tapas_1.orientationDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}"
            }
        },
        "SaisieMasqQT_1": {
            "nodeType": "SaisieMasqQT",
            "position": [
                730,
                -161
            ],
            "inputs": {
                "projectDirectory": "{AperiCloud_1.projectDirectory}",
                "filePath": "{AperiCloud_1.pointCloud}",
                "Attr": "Plan",
                "imagePattern": "{AperiCloud_1.imagePattern}",
                "orientationDir": "{AperiCloud_1.orientationDir}"
            }
        },
        "SaisieMasq_1": {
            "nodeType": "SaisieMasq",
            "position": [
                144,
                -155
            ],
            "inputs": {
                "projectDirectory": "{SaisieBasc_1.projectDirectory}",
                "imagePath": "{SaisieBasc_1.Output}",
                "imagePattern": "{SaisieBasc_1.imagePattern}",
                "orientationDir": "{SaisieBasc_1.Orientation}"
            }
        },
        "C3DC_1": {
            "nodeType": "C3DC",
            "position": [
                924,
                -160
            ],
            "inputs": {
                "projectDirectory": "{SaisieMasqQT_1.projectDirectory}",
                "imagePattern": "{SaisieMasqQT_1.imagePattern}",
                "orientationDir": "{SaisieMasqQT_1.orientationDir}",
                "mode": "BigMac",
                "Masq3D": "{MeshCloudClip_2.Out}"
            }
        },
        "MeshCheck_1": {
            "nodeType": "MeshCheck",
            "position": [
                1348,
                -296
            ],
            "inputs": {
                "projectDirectory": "{TiPunch_1.projectDirectory}",
                "Cloud": "{TiPunch_1.Out}"
            }
        },
        "MeshCloudClip_1": {
            "nodeType": "MeshCloudClip",
            "position": [
                1563,
                -297
            ],
            "inputs": {
                "projectDirectory": "{MeshCheck_1.projectDirectory}",
                "Cloud": "{MeshCheck_1.Out}",
                "3DReg": "{SaisieMasqQT_2.Output Masq}"
            }
        },
        "OriConvV1V2_1": {
            "nodeType": "OriConvV1V2",
            "position": [
                1378,
                -32
            ],
            "inputs": {
                "projectDirectory": "{MeshDev_1.projectDirectory}",
                "In": "{C3DC_1.orientationDir}"
            }
        },
        "RadiomCreateModel_1": {
            "nodeType": "RadiomCreateModel",
            "position": [
                2202,
                -167
            ],
            "inputs": {
                "projectDirectory": "{MeshProjImage_1.projectDirectory}",
                "imageName": "{MeshProjImage_1.imageName}",
                "inputCalib": "{MeshProjImage_1.inputOri}",
                "inputRadModel": "{MeshProjImage_1.OutRadData}",
                "DegIma": 2
            }
        },
        "SaisieMasqQT_2": {
            "nodeType": "SaisieMasqQT",
            "position": [
                1345,
                -434
            ],
            "inputs": {
                "projectDirectory": "{SubSample_1.projectDirectory}",
                "filePath": "{SubSample_1.OutpointCloud}"
            }
        },
        "MeshCloudClip_2": {
            "nodeType": "MeshCloudClip",
            "position": [
                600,
                -10
            ],
            "inputs": {
                "projectDirectory": "{SBGlobBascule_1.projectDirectory}"
            }
        }
    }
}