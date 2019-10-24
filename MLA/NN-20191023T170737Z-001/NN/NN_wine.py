
#-----------------------------------------------------------------
    import pandas as pd
    import numpy as np
#-----------------------------------------------------------------
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
#-----------------------------------------------------------------
    import keras
    from keras.models import Sequential #Sequential Models
    from keras.layers import Dense #Dense Fully Connected Layer Type
#-----------------------------------------------------------------
    
    
   
    wine_df = pd.read_csv('wine.data')
    wine_df.columns = ['Class', 'Alcohol', 'Malic_Acid', 'Ash', 'Alcalinity_of_ash', 'Magnesium', 'Tot_phenols', 'Flavanoids', 'Non_flavanoid_phenols', 'Proanthocyanins', 'Colour', 'Hue', 'OD280/OD315', 'Proline']
#-----------------------------------------------------------------
    X = wine_df.iloc[:,1:14]
    Y = wine_df.iloc[:,0]
#-----------------------------------------------------------------
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
#-----------------------------------------------------------------
    Y=Y-1
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
#-----------------------------------------------------------------
    Y_train = keras.utils.to_categorical(Y_train,3)
    Y_test = keras.utils.to_categorical(Y_test,3)
#-----------------------------------------------------------------
      
    def create_network():
        model = Sequential()
        model.add(Dense(15,input_dim=13,activation='relu'))
        model.add(Dense(8,activation='relu'))
        model.add(Dense(6,activation='relu'))
        model.add(Dense(6,activation='relu'))
        model.add(Dense(4,activation='relu'))
        model.add(Dense(2,activation='relu'))
        model.add(Dense(3,activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
        
        return model
   
	
    
#-----------------------------------------------------------------
  
     model = create_network()
     model.fit(X_train,Y_train, epochs=500, batch_size=10)
     y_pred=model.predict(X_test, batch_size=10, verbose=0)
     scores = model.evaluate(X_test, Y_test)
     print("accuracy=",scores[1])
     
#-----------------------------------------------------------------
   
   
    import graphviz
    from ann_visualizer.visualize import ann_viz
    ann_viz(model, title="Neural Network for Wine Dataset")
#-----------------------------------------------------------------

  