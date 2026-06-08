import sys
import mlflow
import mlflow.sklearn
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from customer_churn_mlops.exception import CustomException
from customer_churn_mlops.logger import logging

from customer_churn_mlops.entity.config_entity import (
    ModelTrainerConfig
)

from customer_churn_mlops.utils.common import (
    save_object
)

from customer_churn_mlops.utils.model_utils import (
    evaluate_models
)



from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

class ModelTrainer:

    def __init__(
        self,
        config: ModelTrainerConfig
    ):
        self.config = config

    def initiate_model_trainer(self):

        try:

            train_arr = np.load(
                self.config.train_data_path
            )

            test_arr = np.load(
                self.config.test_data_path
            )

            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            models = {

            "RandomForest":

            RandomForestClassifier(

                **self.config.params.RandomForest
            ),

            "XGBoost":

            XGBClassifier(

                **self.config.params.XGBoost
            ),

            "LogisticRegression":

            LogisticRegression(

                **self.config.params.LogisticRegression
            )
        }

            model_report = evaluate_models(
                X_train,
                y_train,
                X_test,
                y_test,
                models
            )

            best_model_score = max(
                sorted(model_report.values())
            )

            best_model_name = max(
                model_report,
                key=model_report.get
            )

            best_model = models[
                best_model_name
            ]

            logging.info(
                f"Best Model: {best_model_name}"
            )

            logging.info(
                f"ROC-AUC: {best_model_score}"
            )

            if (
                best_model_score
                <
                self.config.expected_score
            ):
                raise Exception(
                    "No best model found"
                )

            best_model.fit(
                X_train,
                y_train
            )
            y_pred = best_model.predict(X_test)

            y_pred_proba = best_model.predict_proba(
                X_test
            )[:, 1]

            accuracy = accuracy_score(
                y_test,
                y_pred
            )

            precision = precision_score(
                y_test,
                y_pred
            )

            recall = recall_score(
                y_test,
                y_pred
            )

            f1 = f1_score(
                y_test,
                y_pred
            )

            roc_auc = roc_auc_score(
                y_test,
                y_pred_proba
            )

            mlflow.set_experiment(
                "customer_churn_experiment"
            )

            with mlflow.start_run():

                mlflow.log_param(
                    "best_model",
                    best_model_name
                )

                mlflow.log_metric(
                    "accuracy",
                    accuracy
                )

                mlflow.log_metric(
                    "precision",
                    precision
                )

                mlflow.log_metric(
                    "recall",
                    recall
                )

                mlflow.log_metric(
                    "f1_score",
                    f1
                )

                mlflow.log_metric(
                    "roc_auc",
                    roc_auc
                )

                mlflow.sklearn.log_model(
                    best_model,
                    "model"
                )



            save_object(
                self.config.model_path,
                best_model
            )

            logging.info(
                "Model saved successfully"
            )

            return best_model_score

        except Exception as e:
            raise CustomException(e, sys)
        

        