# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:12:10 2019

@author: HP
"""


    import pandas as pd
    import numpy as np
   
    diabetes_df = pd.read_csv('diabetes_csv.csv')
    diabetes_df.describe()
  
    diabetes_df['class']=diabetes_df['class'].replace('tested_negative',0)
    diabetes_df['class']=diabetes_df['class'].replace('tested_positive',1)
    X = diabetes_df.iloc[:,0:8]
    y = diabetes_df.iloc[:,8]
  
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
  
    #Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
   
    
   
    import keras
    from keras.models import Sequential
    from keras.layers import Dense
    
	# Initialising the ANN
    classifier = Sequential()
   
    # Adding the input layer and the first hidden layer
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 8))
    
    # Adding the second hidden layer
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
    
    # Adding the output layer
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
   
    # Compiling the ANN
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
  
    classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)
  
    y_pred = classifier.predict(X_test)
  
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
 
    print(cm)
   
   
    #Import scikit-learn metrics module for accuracy calculation
    from sklearn import metrics
    
    # Model Accuracy: how often is the classifier correct?
    print(\"Accuracy:\",metrics.accuracy_score(y_test, y_pred))
  
    # Model Precision: what percentage of positive tuples are labeled as such?
    print(\"Precision:\",metrics.precision_score(y_test, y_pred))
    
    # Model Recall: what percentage of positive tuples are labelled as such?
    print(\"Recall:\",metrics.recall_score(y_test, y_pred))
   









