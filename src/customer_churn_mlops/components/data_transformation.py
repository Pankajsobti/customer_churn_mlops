import os
import sys
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)

from customer_churn_mlops.logger import logging
from customer_churn_mlops.exception import CustomException

from customer_churn_mlops.entity.config_entity import (
    DataTransformationConfig
)

from customer_churn_mlops.utils.common import (
    save_object
)


class DataTransformation:

    def __init__(
        self,
        config: DataTransformationConfig
    ):
        self.config = config

    def get_data_transformer_object(self):

        try:

            numerical_columns = [
                "SeniorCitizen",
                "tenure",
                "MonthlyCharges",
                "TotalCharges"
            ]

            categorical_columns = [
                "gender",
                "Partner",
                "Dependents",
                "PhoneService",
                "MultipleLines",
                "InternetService",
                "OnlineSecurity",
                "OnlineBackup",
                "DeviceProtection",
                "TechSupport",
                "StreamingTV",
                "StreamingMovies",
                "Contract",
                "PaperlessBilling",
                "PaymentMethod"
            ]

            num_pipeline = Pipeline(
                steps=[
                    (
                        "imputer",
                        SimpleImputer(strategy="median")
                    ),
                    (
                        "scaler",
                        StandardScaler()
                    )
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    (
                        "imputer",
                        SimpleImputer(
                            strategy="most_frequent"
                        )
                    ),
                    (
                        "one_hot_encoder",
                        OneHotEncoder(
                            handle_unknown="ignore"
                        )
                    ),
                    (
                        "scaler",
                        StandardScaler(
                            with_mean=False
                        )
                    )
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    (
                        "num_pipeline",
                        num_pipeline,
                        numerical_columns
                    ),
                    (
                        "cat_pipeline",
                        cat_pipeline,
                        categorical_columns
                    )
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self):

        try:

            train_df = pd.read_csv(
                self.config.input_train_data_path
            )

            test_df = pd.read_csv(
                self.config.input_test_data_path
            )

            train_df = train_df.drop(
                columns=["customerID"]
            )

            test_df = test_df.drop(
                columns=["customerID"]
            )

            train_df["TotalCharges"] = pd.to_numeric(
                train_df["TotalCharges"],
                errors="coerce"
            )

            test_df["TotalCharges"] = pd.to_numeric(
                test_df["TotalCharges"],
                errors="coerce"
            )

            train_df["Churn"] = train_df["Churn"].map(
                {"No": 0, "Yes": 1}
            )

            test_df["Churn"] = test_df["Churn"].map(
                {"No": 0, "Yes": 1}
            )

            target_column = "Churn"

            X_train = train_df.drop(
                columns=[target_column]
            )

            y_train = train_df[target_column]

            X_test = test_df.drop(
                columns=[target_column]
            )

            y_test = test_df[target_column]

            preprocessor = (
                self.get_data_transformer_object()
            )

            X_train_arr = preprocessor.fit_transform(
                X_train
            )

            X_test_arr = preprocessor.transform(
                X_test
            )

            train_arr = np.c_[
                X_train_arr,
                np.array(y_train)
            ]

            test_arr = np.c_[
                X_test_arr,
                np.array(y_test)
            ]

            save_object(
                self.config.preprocessor_path,
                preprocessor
            )

            np.save(
                self.config.train_data_path,
                train_arr
            )

            np.save(
                self.config.test_data_path,
                test_arr
            )

            logging.info(
                "Data Transformation Completed"
            )

            return (
                train_arr,
                test_arr,
                self.config.preprocessor_path
            )

        except Exception as e:
            raise CustomException(e, sys)