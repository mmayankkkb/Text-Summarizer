# from TextSummarizer.logger import logger

# # logger.info("Welcome to our Custom Log")
# from TextSummarizer.logging import logger

# logger.info("Welcome To the Custom Log !!!!!!")


from TextSummarizer.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> STAGE {STAGE_NAME} STARTED <<<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    
    logger.info(f" >>>>> STAGE {STAGE_NAME} COMPLETED <<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e