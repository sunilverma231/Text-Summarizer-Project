import sys
import shutil
from pathlib import Path

# Ensure local src/ is on the path before importing pipelines (when package isn't installed)
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

# Optional: Clean artifacts folder for fresh run (comment out to keep old artifacts)
artifacts_dir = Path(__file__).resolve().parent / "artifacts"
if artifacts_dir.exists():
    shutil.rmtree(artifacts_dir)

from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainPipeline
from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainPipeline
from text_summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from text_summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainPipeline
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

stage_name = "Model Training Stage"
try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    from text_summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error in stage {stage_name}")
    raise e 

stage_name = "Model Evaluation Stage"

try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    model_evaluation = ModelEvaluationTrainPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error in stage {stage_name}")
    raise e