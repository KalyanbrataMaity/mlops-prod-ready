import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from us_visa.exception import USvisaException
from us_visa.logger import logging


class DataIngestion:
    def __init__(self):
        """
        """
        pass


    def export_data_into_feature_store(self) -> DataFrame:
        """
        """
        try:
            logging.info("Starting export data from mongodb")
            
        except Exception as e:
            raise USvisaException(e, sys) from e

    
