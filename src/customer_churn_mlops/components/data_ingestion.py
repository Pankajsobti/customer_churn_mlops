import os
import zipfile
import subprocess

from customer_churn_mlops.logger import logging
from customer_churn_mlops.entity.config_entity import DataIngestionConfig
import pandas as pd

from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):

        if os.path.exists(self.config.local_data_file):
            logging.info("Dataset already exists.")
            return

        logging.info("Downloading dataset from Kaggle")

        command = [
            "kaggle",
            "datasets",
            "download",
            "-d",
            self.config.dataset_name,
            "-p",
            self.config.root_dir
        ]

        subprocess.run(command, check=True)

        logging.info("Dataset downloaded successfully")

    def extract_zip_file(self):

        zip_file_path = self.config.local_data_file

        unzip_path = self.config.unzip_dir

        logging.info("Extracting dataset")

        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

        logging.info("Dataset extracted successfully")

    def train_test_split_data(self):

        csv_file = os.path.join(
            self.config.unzip_dir,
            "WA_Fn-UseC_-Telco-Customer-Churn.csv"
        )

        df = pd.read_csv(csv_file)

        train_set, test_set = train_test_split(
            df,
            test_size=0.2,
            random_state=42
        )

        train_set.to_csv(
            self.config.train_data_path,
            index=False
        )

        test_set.to_csv(
            self.config.test_data_path,
            index=False
        )

        logging.info("Train Test Split Completed")