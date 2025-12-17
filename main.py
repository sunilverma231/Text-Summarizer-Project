import sys
from pathlib import Path

# Ensure local src/ is on the path when running directly
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from text_summarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e: 
    logger.exception(f"Error in stage {STAGE_NAME}")
    raise e