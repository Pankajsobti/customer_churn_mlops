from customer_churn_mlops.utils.common import read_yaml

from customer_churn_mlops.constants import (
    CONFIG_FILE_PATH,
    PARAMS_FILE_PATH,
    SCHEMA_FILE_PATH
)


class ConfigurationManager:

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH
    ):

        self.config = read_yaml(config_filepath)

        self.params = read_yaml(params_filepath)

        self.schema = read_yaml(schema_filepath)