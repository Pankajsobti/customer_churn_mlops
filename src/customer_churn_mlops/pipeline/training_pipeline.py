from customer_churn_mlops.config.configuration import ConfigurationManager

from customer_churn_mlops.components.data_ingestion import DataIngestion

from customer_churn_mlops.components.data_validation import (
    DataValidation
)

from customer_churn_mlops.components.data_transformation import (
    DataTransformation
)



from customer_churn_mlops.components.model_trainer import (
    ModelTrainer
)


from customer_churn_mlops.components.model_evaluation import (
    ModelEvaluation
)


class TrainingPipeline:

    def __init__(self):
        pass

    def start_data_ingestion(self):

        config = ConfigurationManager()

        data_ingestion_config = (
            config.get_data_ingestion_config()
        )

        data_ingestion = DataIngestion(
            data_ingestion_config
        )

        data_ingestion.download_file()

        data_ingestion.extract_zip_file()

        data_ingestion.train_test_split_data()

    def start_data_validation(self):

        config = ConfigurationManager()

        validation_config = (
            config.get_data_validation_config()
        )

        validation = DataValidation(
            validation_config
        )

        validation.validate_all_columns()


    def start_data_transformation(self):

        config = ConfigurationManager()

        transformation_config = (
            config.get_data_transformation_config()
        )

        transformation = DataTransformation(
            transformation_config
        )

        transformation.initiate_data_transformation()

    def start_model_training(self):

        config = ConfigurationManager()

        trainer_config = (
            config.get_model_trainer_config()
        )

        trainer = ModelTrainer(
            trainer_config
        )

        trainer.initiate_model_trainer()


    def start_model_evaluation(self):

        config = ConfigurationManager()

        evaluation_config = (
            config.get_model_evaluation_config()
        )

        evaluation = ModelEvaluation(
            evaluation_config
        )

        metrics = (
            evaluation.initiate_model_evaluation()
        )

        print(metrics)