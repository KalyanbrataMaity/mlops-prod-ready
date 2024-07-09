import os 
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise USvisaException(e, sys) from e
    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            yaml.dump(content, yaml_file, default_flow_style=False)

    except Exception as e:
        raise USvisaException(e, sys) from e

def load_object(file_path: str) -> object:
    logging.info("Entered the load_object method of utils")

    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        
        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise USvisaException(e, sys) from e


def save_numpy_array_data(file_path: str, array: np.array):
    """ 
    Saves a numpy array data to a file.
    file_path: str location of file to save
    array: np.array data to be saved
    """
    logging.info("Entered the save_numpy_array_data method of utils")

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_path, array)

        logging.info("Exited the save_numpy_array_data method of utils")

    except Exception as e:
        raise USvisaException(e, sys) from e


def load_nummpy_array_data(file_path: str) -> np.array:
    """ 
    Loads a numpy array data from a file.
    file_path: str location of file to load
    return: np.array data loaded
    """
    logging.info("Entered the load_nummpy_array_data method of utils")

    try:
        with open(file_path, 'rb') as file_obj:
            array = np.load(file_obj)

        logging.info("Exited the load_nummpy_array_data method of utils")

        return array

    except Exception as e:
        raise USvisaException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save object method of utils")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save object method of utils")

    except Exception as e:
        raise USvisaException(e, sys) from e


def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """ 
    Drops specified columns from a DataFrame.
    df: DataFrame to drop columns from
    cols: list of columns to drop
    return: DataFrame with specified columns dropped
    """
    logging.info("Entered the drop_columns method of utils")

    try:
        df= df.drop(cols, axis=1)

        logging.info("Exited the drop_columns method of utils")

        return df

    except Exception as e:
        raise USvisaException(e, sys) from e