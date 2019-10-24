# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:06:56 2019

@author: HP
"""

import os
os.environ["PATH"] += os.pathsep + 'C:/Users/HP/Anaconda3/Lib/site-packages/graphviz'


    import pandas as pd
    import numpy as np
   
    wine_df = pd.read_csv('wine.data')
    wine_df.columns = ['Class', 'Alcohol', 'Malic_Acid', 'Ash', 'Alcalinity_of_ash', 'Magnesium', 'Tot_phenols', 'Flavanoids', 'Non_flavanoid_phenols', 'Proanthocyanins', 'Colour', 'Hue', 'OD280/OD315', 'Proline']
   
    X = wine_df.iloc[:,1:14]
    y = wine_df.iloc[:,0]
 
    print(np.unique(y))
  
    wine_df.shape
  
    #One Hot Encode our Y:
    from sklearn.preprocessing import LabelBinarizer
    encoder = LabelBinarizer()
    Y = encoder.fit_transform(y)
  
   
    from keras.models import Sequential #Sequential Models
    from keras.layers import Dense #Dense Fully Connected Layer Type
    from keras.optimizers import SGD #Stochastic Gradient Descent Optimizer
   
	def create_network():
		model = Sequential()
		model.add(Dense(15, input_shape=(13,), activation='relu'))
		model.add(Dense(3, activation='softmax'))
		#stochastic gradient descent
		sgd = SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
		model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
		
		return model
  
  
  
    
     neural_network = create_network()
     neural_network.fit(X,Y, epochs=500, batch_size=10)
   
   
    import numpy as np
    np.set_printoptions(suppress=True)
    
    neural_network.predict(X[0:10], batch_size=32, verbose=0)
   
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
  
   
    neural_network = create_network()
    neural_network.fit(X_scaled,Y, epochs=100, batch_size=10)
   
    neural_network.predict(X[0:10], batch_size=32, verbose=0)
   
    scores = neural_network.evaluate(X_scaled, Y)
    print(\"\\n%s: %.2f%%\" % (neural_network.metrics_names[1], scores[1]*100))
   
    import graphviz
    from ann_visualizer.visualize import ann_viz
    ann_viz(neural_network, title="Neural Network for Wine Dataset")
  