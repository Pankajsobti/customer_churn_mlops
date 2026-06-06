import pandas as pd

from customer_churn_mlops.utils.common import (
    load_object
)


class PredictionPipeline:

    def __init__(self):

        self.model = load_object(
            "artifacts/model_trainer/model.pkl"
        )

        self.preprocessor = load_object(
            "artifacts/data_transformation/preprocessor.pkl"
        )

    def predict(self, data: dict):

        df = pd.DataFrame([data])

        processed_data = self.preprocessor.transform(df)

        prediction = self.model.predict(
            processed_data
        )

        return int(prediction[0])