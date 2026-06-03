import os
from pathlib import Path

project_name = "customer_churn_mlops"

list_of_files = [

    ".github/workflows/ci.yml",

    "data/.gitkeep",
    "notebooks/.gitkeep",
    "artifacts/.gitkeep",
    "logs/.gitkeep",
    "experiments/.gitkeep",
    "tests/__init__.py",

    f"src/{project_name}/__init__.py",

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/constants/__init__.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/model_utils.py",

    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",

    "app/__init__.py",
    "app/main.py",

    "params.yaml",
    "schema.yaml",

    "requirements.txt",
    "setup.py",

    "Dockerfile",
    "dvc.yaml",

    ".gitignore",
    "README.md",

    "main.py"
]

for filepath in list_of_files:

    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

print("Project structure created successfully.")