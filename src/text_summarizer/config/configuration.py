from text_summarizer.constants import *
from text_summarizer.utils.common import read_yaml, create_directories
from text_summarizer.entity import DataIngestionConfig
import os
from pathlib import Path

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ):
        print(f"DEBUG - ConfigurationManager received config_filepath: {config_filepath}")
        print(f"DEBUG - ConfigurationManager received params_filepath: {params_filepath}")
        
        # Convert relative paths to absolute
        if not config_filepath.is_absolute():
            config_filepath = Path(os.getcwd()) / config_filepath
        if not params_filepath.is_absolute():
            params_filepath = Path(os.getcwd()) / params_filepath
        
        print(f"DEBUG - After path conversion, config_filepath: {config_filepath}")
        print(f"DEBUG - After path conversion, params_filepath: {params_filepath}")
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir]) 
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion_config