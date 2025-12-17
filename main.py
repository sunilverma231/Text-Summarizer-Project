import sys
from pathlib import Path
from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainPipeline
from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainPipeline
from text_summarizer.logging import logger


# Ensure local src/ is on the path when running directly
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

STAGE_NAME = "Data Ingestion Stage"
try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e: 
    logger.exception(f"Error in stage {STAGE_NAME}")
    raise e


STAGE_NAME = "Data Validation Stage"
try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e: 
    logger.exception(f"Error in stage {STAGE_NAME}")
    raise e


STAGE_NAME = "Data Transformation Stage"
try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainPipeline
    data_transformation = DataTransformationTrainPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e: 
    logger.exception(f"Error in stage {STAGE_NAME}")
    raise e