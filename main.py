from customer_churn_mlops.pipeline.training_pipeline import (
    TrainingPipeline
)

pipeline = TrainingPipeline()

pipeline.start_data_ingestion()

pipeline.start_data_validation()

pipeline.start_data_transformation()

pipeline.start_model_training()

pipeline.start_model_evaluation()

print("Data ingestion completed.")
