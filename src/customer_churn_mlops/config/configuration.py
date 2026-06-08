from customer_churn_mlops.utils.common import read_yaml

from customer_churn_mlops.constants import (
    CONFIG_FILE_PATH,
    PARAMS_FILE_PATH,
    SCHEMA_FILE_PATH
)

from pathlib import Path

from customer_churn_mlops.entity.config_entity import (
    DataIngestionConfig
)

from customer_churn_mlops.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig
)


from customer_churn_mlops.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig
)



from customer_churn_mlops.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

from customer_churn_mlops.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig
)


class ConfigurationManager:

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH
    ):

        self.config = read_yaml(config_filepath)

        self.params = read_yaml(params_filepath)

        self.schema = read_yaml(schema_filepath)

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        Path(config.root_dir).mkdir(
            parents=True,
            exist_ok=True
        )

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            dataset_name=config.dataset_name,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path
        )

        return data_ingestion_config    
    
    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config.data_validation

        schema = self.schema.columns

        Path(config.root_dir).mkdir(
            parents=True,
            exist_ok=True
        )

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            unzip_data_dir=self.config.data_ingestion.unzip_dir,
            all_schema=schema
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation

        Path(config.root_dir).mkdir(
            parents=True,
            exist_ok=True
        )

        return DataTransformationConfig(
        root_dir=config.root_dir,

        input_train_data_path=config.input_train_data_path,
        input_test_data_path=config.input_test_data_path,

        train_data_path=config.train_data_path,
        test_data_path=config.test_data_path,

        preprocessor_path=config.preprocessor_path
    )

    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config = self.config.model_trainer
        params = self.params

        Path(config.root_dir).mkdir(
            parents=True,
            exist_ok=True
        )

        return ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            expected_score=config.expected_score,
            params=params
        )
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:

        config = self.config.model_evaluation

        Path(config.root_dir).mkdir(
            parents=True,
            exist_ok=True
        )

        return ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metric_file_name=config.metric_file_name
        )