import os
import pandas as pd

from customer_churn_mlops.logger import logging
from customer_churn_mlops.entity.config_entity import (
    DataValidationConfig
)


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:

        validation_status = True

        data = pd.read_csv(
            os.path.join(
                self.config.unzip_data_dir,
                "WA_Fn-UseC_-Telco-Customer-Churn.csv"
            )
        )

        all_cols = list(data.columns)

        all_schema = self.config.all_schema.keys()

        for col in all_cols:

            if col not in all_schema:
                validation_status = False

                with open(
                    self.config.status_file,
                    "w"
                ) as f:

                    f.write(
                        f"Validation Status: {validation_status}"
                    )

        with open(
            self.config.status_file,
            "w"
        ) as f:

            f.write(
                f"Validation Status: {validation_status}"
            )

        return validation_status