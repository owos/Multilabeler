"""
This package gives the prediction of two dependent features/labels y1 and y2.
borne out of the idea to break the striction of predicting just one y

"""

# Author: Abraham Owodunni <owoowodunniabraham@gmail.com>

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class BilabelClassifier:
    """
    A two label prediction classifer.
    A BilabelClassifier takes in data (X) and ouputs two depedent features
    (y1, y2) from the data after training. The target features required are of 
    categorical data types. 

    Arguements
    ----------
    model (class): The already instantiated algorithm which the model is to be
    built with. The algorithms should be able to handle binary classifications.
    
    Example
    -------
    m = BilabelClassifier(sklearn.linear_model.RandomRandomForestClassifier())

    Check repo https://github.com/owos/Multilabel
    """

    def __init__(self, model):
        self.model = model
        self.X_train  = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.encoder1 = LabelEncoder()
   
    def fit(self, X_train, y_train):
        """
        Parameters
        ----------
        X_train (DataFrame/array): array-like or sparse matrix with n shape.
        y_train (Pandas DataFrame): a pandas DataFrame with n samples and two 
        columns for the two featuresto be predicted.

        
        Returns
        -------
        self: obeject
       
        Check repo https://github.com/owos/Multilabel
        """

        #converting y1 and y2 to str
        y_train = y_train.astype("str")

        #combining the columns
        y_train["y1y2"] = y_train[list(y_train.columns)[0]] + y_train[list(y_train.columns)[1]]
        self.y_train = y_train
        self.X_train = X_train
        
        #encoding the column
        self.y_train["y"] = self.encoder1.fit_transform(self.y_train["y1y2"])

        self.model = self.model.fit(self.X_train, self.y_train["y"])
        return self.model

    def predict(self, X_test):
        """
        Predict classification y1 and y2 for X_test given.

        Paramaters
        ----------
        X_test(DataFrame/array): array-like or sparse matrix with n samples.
        
        Returns
        -------
        y (padans DataFrame): The predicted classes with two columns or series
        """
        self.X_test = X_test
        #predicting with the model
        self.model_predict = self.model.predict(self.X_test) 
        #converting the model output back to 1,2 combinations
        inverser = list(self.encoder1.inverse_transform(self.model_predict))
        #extracting the first output
        y_1 = [int(y) for x in inverser for y in list(x)[0]]
        #extracting the second output
        y_2 = [int(y) for x in inverser for y in list(x)[1]] 
        #converting to dataframe
        y_pred = pd.DataFrame({list(self.y_train.columns)[0]: y_1, 
                                list(self.y_train.columns)[1]: y_2}) 
        return y_pred