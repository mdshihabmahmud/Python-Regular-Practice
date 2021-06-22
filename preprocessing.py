#Data Preprocessing

#importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,0:3].values
y = dataset.iloc[:,3].values

#taking care of missing values
from sklearn.impute import SimpleImputer

missingvalues = SimpleImputer(missing_values=np.nan, strategy = 'mean', verbose = 0) 
missingvalues = missingvalues.fit(x[:,1:3])
x[:,1:3] = missingvalues.transform(x[:,1:3])


#independent variables
#level encode

#from sklearn.preprocessing import LabelEncoder
#Labelencoder_x = LabelEncoder()
#x[:,0] = Labelencoder_x.fit_transform(x[:,0])

#OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder = "passthrough")
x = np.array(ct.fit_transform(x), dtype = np.float)


#dependent variables
#level encode

from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


#train test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.2, random_state=0)

#feature Scaling
from sklearn.preprocessing import StandardScaler

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

                      



