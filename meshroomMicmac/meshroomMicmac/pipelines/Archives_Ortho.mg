{
    "header": {
        "pipelineVersion": "2.2",
        "releaseVersion": "2023.3.0-develop",
        "fileVersion": "1.1",
        "template": true,
        "nodesVersions": {
            "TapiocaMulScale": "1.1.1",
            "Tapas": "1.1.1",
            "Tawny": "1.1.1",
            "SaisieMasq": "1.1.1",
            "Malt": "1.0",
            "Tarama": "0.0"
        }
    },
    "graph": {
        "Tapas_1": {
            "nodeType": "Tapas",
            "position": [
                335,
                -173
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
                128,
                -162
            ],
            "inputs": {
                "projectDirectory": "ECRIRE_CHEMIN_DOSSIER_IMAGES",
                "imagePattern": ".*[0-9].(jpg|jpeg|JPG|JPEG|png|PNG|tif|tiff|TIF|TIFF)",
                "imageSizeLowResolution": 400,
                "wallisFilter": "@SFS"
            }
        },
        "Tarama_1": {
            "nodeType": "Tarama",
            "position": [
                540,
                -157
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}",
                "orientation": "{Tapas_1.orientationDirectory}"
            }
        },
        "Malt_1": {
            "nodeType": "Malt",
            "position": [
                947,
                -174
            ],
            "inputs": {
                "projectDirectory": "{SaisieMasq_1.projectDirectory}",
                "imagePattern": "{SaisieMasq_1.imagePattern}",
                "orientation": "{SaisieMasq_1.orientationDir}",
                "waitFor": "{SaisieMasq_1.xmlMeasures}",
                "NbVi": 2,
                "DefCor": 0.0,
                "CostTrans": 4.0
            }
        },
        "Tawny_1": {
            "nodeType": "Tawny",
            "position": [
                1147,
                -166
            ],
            "inputs": {
                "projectDirectory": "{Malt_1.projectDirectory}",
                "orthoDirectory": "Ortho-MEC-Malt",
                "waitFor": "{Malt_1.IsDone}"
            }
        },
        "SaisieMasq_1": {
            "nodeType": "SaisieMasq",
            "position": [
                747,
                -163
            ],
            "inputs": {
                "projectDirectory": "{Tarama_1.projectDirectory}",
                "imagePath": "\"./TA/TA_LeChantier.tif\"",
                "imagePattern": "{Tarama_1.imagePattern}",
                "orientationDir": "{Tarama_1.orientation}",
                "waitFor": "{Tarama_1.outputDirectory}"
            }
        }
    }
}