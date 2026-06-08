from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    root_dir: str
    dataset_name: str
    local_data_file: str
    unzip_dir: str
    train_data_path: str
    test_data_path: str


@dataclass
class DataValidationConfig:
    root_dir: str
    status_file: str
    unzip_data_dir: str
    all_schema: dict


@dataclass
class DataTransformationConfig:
    root_dir: str

    input_train_data_path: str
    input_test_data_path: str

    train_data_path: str
    test_data_path: str

    preprocessor_path: str


@dataclass
class ModelTrainerConfig:
    root_dir: str

    train_data_path: str
    test_data_path: str

    model_path: str

    expected_score: float

    params: dict


@dataclass
class ModelEvaluationConfig:
    root_dir: str
    test_data_path: str
    model_path: str
    metric_file_name: str