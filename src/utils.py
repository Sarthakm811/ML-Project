import os 
import sys 
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score



def save_object(file_path:str, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train, y_train, X_test, y_test, models:dict):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            model_name = list(models.keys())[i]

            # Train the model
            model.fit(X_train, y_train)

            # Predicting the test set results
            y_test_pred = model.predict(X_test)

            # Getting the r2 score for the model
            r2_square = r2_score(y_test, y_test_pred)

            report[model_name] = r2_square

        return report

    except Exception as e:
        raise CustomException(e, sys)

    