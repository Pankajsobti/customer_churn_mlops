import json
import sys
import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from customer_churn_mlops.exception import CustomException
from customer_churn_mlops.logger import logging

from customer_churn_mlops.entity.config_entity import (
    ModelEvaluationConfig
)

from customer_churn_mlops.utils.common import (
    load_object
)


class ModelEvaluation:

    def __init__(
        self,
        config: ModelEvaluationConfig
    ):
        self.config = config

    def initiate_model_evaluation(self):

        try:

            test_arr = np.load(
                self.config.test_data_path
            )

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            model = load_object(
                self.config.model_path
            )

            y_pred = model.predict(X_test)

            y_pred_proba = model.predict_proba(
                X_test
            )[:, 1]

            metrics = {

                "accuracy":
                    float(
                        accuracy_score(
                            y_test,
                            y_pred
                        )
                    ),

                "precision":
                    float(
                        precision_score(
                            y_test,
                            y_pred
                        )
                    ),

                "recall":
                    float(
                        recall_score(
                            y_test,
                            y_pred
                        )
                    ),

                "f1_score":
                    float(
                        f1_score(
                            y_test,
                            y_pred
                        )
                    ),

                "roc_auc":
                    float(
                        roc_auc_score(
                            y_test,
                            y_pred_proba
                        )
                    )
            }

            with open(
                self.config.metric_file_name,
                "w"
            ) as f:

                json.dump(
                    metrics,
                    f,
                    indent=4
                )

            logging.info(
                "Model Evaluation Completed"
            )

            return metrics

        except Exception as e:
            raise CustomException(e, sys)