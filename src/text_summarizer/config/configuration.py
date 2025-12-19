from text_summarizer.constants import *
from text_summarizer.utils.common import read_yaml, create_directories
from text_summarizer.entity import DataIngestionConfig, DataTransformationConfig
from text_summarizer.entity import DataValidationConfig
import os
from pathlib import Path

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ):
        # Convert relative paths to absolute
        if not config_filepath.is_absolute():
            config_filepath = Path(os.getcwd()) / config_filepath
        if not params_filepath.is_absolute():
            params_filepath = Path(os.getcwd()) / params_filepath

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
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir]) 
        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            status_file=config.STATUS_FILE,
            All_REQUIRED_FILES=config.REQUIRED_FILES,
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir]) 
        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name,
        )
        return data_transformation_config
    
    def get_model_trainer_config(self):
        config = self.config.model_trainer
        create_directories([config.root_dir]) 
        from text_summarizer.entity import ModelTrainerConfig
        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            model_ckpt=config.model_ckpt,
            num_train_epochs=config.num_train_epochs,
            learning_rate=config.learning_rate,
            train_batch_size=config.train_batch_size,
            eval_batch_size=config.eval_batch_size,
            weight_decay=config.weight_decay,
            warmup_steps=config.warmup_steps,
            logging_dir=config.logging_dir,
        )
        return model_trainer_config
    