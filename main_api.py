from fastapi import FastAPI

from pydantic import BaseModel

from customer_churn_mlops.pipeline.prediction_pipeline import (
    PredictionPipeline
)

app = FastAPI()


class CustomerData(BaseModel):

    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():

    return {
        "message":
        "Customer Churn Prediction API Running"
    }


@app.post("/predict")
def predict(data: CustomerData):

    pipeline = PredictionPipeline()

    prediction = pipeline.predict(
        data.dict()
    )

    result = (
        "Customer Will Churn"
        if prediction == 1
        else
        "Customer Will Not Churn"
    )

    return {
        "prediction": result
    }