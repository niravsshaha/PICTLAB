
    import numpy as np
    import pandas as pd
#-----------------------------------------------------------------
    from sklearn.datasets import load_boston
#-----------------------------------------------------------------    
    from keras.models import Sequential #Sequential Models
    from keras.layers import Dense
#-----------------------------------------------------------------
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
#-----------------------------------------------------------------
    import graphviz
    from ann_visualizer.visualize import ann_viz
#-----------------------------------------------------------------
    
    boston = load_boston()
    X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size = 0.2, random_state = 0)
#-----------------------------------------------------------------
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
#-----------------------------------------------------------------
    
    def build_model():
        model = Sequential()
        model.add(Dense(64, activation='relu', input_dim=13))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(1))
        model.compile(optimizer='adam',loss='mse',metrics=['mae'])
        
        return model
    
#-----------------------------------------------------------------
    
	model = build_model()
    
    model.fit(X_train,y_train,batch_size=25,epochs=500)   
    
    y_pred=model.predict(X_test)
    
    scores = model.evaluate(X_test,y_test)
    
    print(scores)

#-----------------------------------------------------------------
   ann_viz(model, title="Neural Network for Boston Dataset")
#-----------------------------------------------------------------
