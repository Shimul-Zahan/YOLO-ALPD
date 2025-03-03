# This is for web application

import sys
import cv2
import numpy as np
import pandas as pd
import seaborn as sns
# import tensorflow
import matplotlib.pyplot as plt
from exception import CustomException
from logger import logging

logging.basicConfig(level=logging.INFO)

try:
    5/0
    logging.info("Logging has started!!!") 
    print("Hello World")
except Exception as ex:
    logging.error("An error occurred: %s", str(ex))
    raise CustomException(ex, sys)