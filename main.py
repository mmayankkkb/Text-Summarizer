# from TextSummarizer.logger import logger

# # logger.info("Welcome to our Custom Log")
# from TextSummarizer.logging import logger

# logger.info("Welcome To the Custom Log !!!!!!")

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
from TextSummarizer.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger
from TextSummarizer.pipline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipline.stage_03_data_transformation import DataTransformationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    
    logger.info(f" >>>>> STAGE {STAGE_NAME} COMPLETED <<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    data_validation= DataValidationTrainingPipeline()
    data_validation.main()
    
    logger.info(f" >>>>> STAGE {STAGE_NAME} COMPLETED <<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    data_transformation= DataTransformationTrainingPipeline()
    data_transformation.main()
    print("Reached after DataTransformation init")
    logger.info(f" >>>>> STAGE {STAGE_NAME} COMPLETED <<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e