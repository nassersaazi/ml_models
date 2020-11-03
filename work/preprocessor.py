
import config
import sys
import re
import time
import math
import warnings
warnings.filterwarnings('ignore')


import pandas as pd
import seaborn as sns
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
import numpy as np
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
style.use('fivethirtyeight')


class Preprocessor:
    def __init__(self,df):
        self.df = df
    
    def __str__(self):
        pass
    

    def overview(self):
        print(f'\nDataset contains {self.df.shape[0]} rows and {self.df.shape[1]} columns')
        print(f'\nData types of the raw (uncleaned) data:\n{self.df.dtypes}')
        cat,num = self.column_types()
        print(f'\nCategorical features of the dataset: {cat}\n\nNumeric features of the dataset: {num}')
        print(f'\nChecking for features with null values...\n\n{self.df.isnull().sum().sort_values(ascending=False)}' )
    
    
    def show_category(self,df,column,value):
        """
        display rows of a particular category
       :param df: pandas dataframe
       :param column: column which contains selected category
       :param value: selected category
       :return value_df: rows of selected category   
        """
        value_df = df.loc[df[column] == value]
        return value_df

  
    def column_types(self):
        """
        distinguish categorical and numerical columns
       :param df: pandas dataframe
       :return cat_cols, num_cols: two lists, categorical and numerical variables   
        """
        cat_cols = []
        num_cols = []
        
        for y in self.df.columns:
            if (self.df[y].dtype == object):
                cat_cols.append(y)
            else:
                num_cols.append(y)
        
        return cat_cols, num_cols

    
    

    
    def print_exception_message(self,message_orientation="horizontal"):
        """
        print full exception message
       :param message_orientation: horizontal or vertical
       :return None   
        """
        try:
            exc_type, exc_value, exc_tb = sys.exc_info()           
            file_name, line_number, procedure_name, line_code =  traceback.extract_tb(exc_tb)[-1]      
            time_stamp = " [Time Stamp]: " + str(time.strftime(" %Y-%m-%d %I:%M:%S %p"))
            file_name = " [File Name]: " + str(file_name)
            procedure_name = " [Procedure Name]: " +  str(procedure_name)
            error_message = " [Error Message]: " + str(exc_value)       
            error_type = " [Error Type]: " + str(exc_type)                   
            line_number = " [Line Number]: " + str(line_number)               
            line_code = " [Line Code]: " + str(line_code)
            if (message_orientation == config.HORIZONTAL):
                print( "An error occurred:{};{};{};{};{};{}; {}".format(time_stamp, file_name, procedure_name, 
                   error_message, error_type, line_number, line_code))
            elif (message_orientation == config.VERTICAL):
                print( "An error occurred:\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(time_stamp, file_name, 
                   procedure_name, error_message, error_type,        
                   line_number, line_code))
            else:
                pass                   
        except:
            exception_message = sys.exc_info()[0]
            print("An error occurred. {}".format(exception_message))

    def tune_hyperparameter_model(self,ml_model, X_train, y_train, hyper_parameter_candidates, scoring_parameter ,
                                  cv_fold, search_cv_type="grid"):   
        """
        apply grid search cv and randomized search cv algorithms to find optimal hyperparameters model 
        :param ml_model: defined machine learning model
        :param X_train: feature training data
        :param y_train: target (label) training data
        :param hyper_parameter_candidates: dictionary of hyperparameter candidates
        :param scoring_parameter: parameter that controls what metric to apply to the evaluated model
        :param cv_fold: number of cv divided folds
        :param search_cv_type: type of search cv (gridsearchcv or randomizedsearchcv)
        :return classifier_model: defined classifier model
        """
        try:
            if (search_cv_type==config.GRID_SEARCH_CV):
                classifier_model = GridSearchCV(estimator=ml_model, param_grid=hyper_parameter_candidates, 
                   scoring=scoring_parameter, cv=cv_fold)
            elif (search_cv_type==config.RANDOMIZED_SEARCH_CV):
                classifier_model =  RandomizedSearchCV(estimator=ml_model, param_distributions=hyper_parameter_candidates, 
                   scoring=scoring_parameter, cv=cv_fold)
            
            classifier_model.fit(X_train, y_train)
        except:
            print_exception_message()
        return classifier_model
