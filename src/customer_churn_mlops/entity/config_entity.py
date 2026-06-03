from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    root_dir: str
    source_url: str
    local_data_file: str
    unzip_dir: str


@dataclass
class DataValidationConfig:
    root_dir: str
    STATUS_FILE: str
    unzip_data_dir: str
    all_schema: dict


@dataclass
class DataTransformationConfig:
    root_dir: str
    data_path: str
    preprocessor_path: str


@dataclass
class ModelTrainerConfig:
    root_dir: str
    train_data_path: str
    test_data_path: str
    model_name: str


@dataclass
class ModelEvaluationConfig:
    root_dir: str
    test_data_path: str
    model_path: str
    metric_file_name: str