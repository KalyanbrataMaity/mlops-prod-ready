import sys 
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion

from us_visa.entity.config_enity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact 



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifact
        
        except Exception as e:
            raise USvisaException(e, sys) from e
    
        
    def run_pipeline(self) -> None:
        """
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
            raise USvisaException(e, sys) from e