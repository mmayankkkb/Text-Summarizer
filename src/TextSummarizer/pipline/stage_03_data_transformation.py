from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging import logger
from TextSummarizer.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            logger.info("Transformation initialization")
            data_transformation = DataTransformation(config=data_transformation_config)
            logger.info("Transformation initialization Done")
            data_transformation.create_dirs_files()
            logger.info("Created dirs from main Done")
            data_transformation.convert()
            print("Converting Done")
        except Exception as e:
            logger.info("Failed in stage 03")
            raise e 
