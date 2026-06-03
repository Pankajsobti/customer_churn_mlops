import os
import yaml
import joblib

from box import ConfigBox


def read_yaml(path_to_yaml: str) -> ConfigBox:

    with open(path_to_yaml, "r") as yaml_file:
        content = yaml.safe_load(yaml_file)

    return ConfigBox(content)


def save_object(file_path, obj):

    dir_path = os.path.dirname(file_path)

    os.makedirs(dir_path, exist_ok=True)

    joblib.dump(obj, file_path)


def load_object(file_path):

    return joblib.load(file_path)