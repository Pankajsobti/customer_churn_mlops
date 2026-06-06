import pandas as pd

df = pd.read_csv(
    "artifacts/data_ingestion/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

print(df["Churn"].unique())