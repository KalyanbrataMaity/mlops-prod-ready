from us_visa.configuration.mongodb_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import USvisaException
import sys 
from typing import Optional
import pandas as pd
import numpy as np


class USvisaData:
    """
    """

    def __init__(self):
        
        """
        """
        try:
            self.mongodb_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e, sys)
        
    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        exports entire collection as dataframe
        return pd.DataFrame of collection
        """
        try:
            if database_name:
                collection = self.mongodb_client[database_name][collection_name]
            else:
                collection = self.mongodb_client.database[collection_name]
            
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            return df
        
        except Exception as e:
            raise USvisaException(e, sys)
