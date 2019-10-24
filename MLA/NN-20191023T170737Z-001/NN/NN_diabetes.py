

#---------------------------------------------------------------------------
    import pandas as pd
    import numpy as np
#---------------------------------------------------------------------------
    from sklearn.model_selection import train_test_split
    from sklearn import metrics
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import confusion_matrix,accuracy_score
#---------------------------------------------------------------------------
    import keras
    from keras.models import Sequential
    from keras.layers import Dense
#---------------------------------------------------------------------------
    import graphviz
    from ann_visualizer.visualize import ann_viz
#---------------------------------------------------------------------------
    diabetes_df = pd.read_csv('diabetes_csv.csv')
    diabetes_df.describe()
#---------------------------------------------------------------------------
    diabetes_df['class']=diabetes_df['class'].replace('tested_negative',0)
    diabetes_df['class']=diabetes_df['class'].replace('tested_positive',1)
    X = diabetes_df.iloc[:,0:8]
    y = diabetes_df.iloc[:,8]
#---------------------------------------------------------------------------
  
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#---------------------------------------------------------------------------
    #Feature Scaling
    
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
#---------------------------------------------------------------------------
    
   
	# Initialising the ANN
    def create_network():
        
        classifier = Sequential()
    # Adding the input layer and the first hidden layer
        classifier.add(Dense(units = 4, activation = 'relu', input_dim = 8))
    # Adding the second hidden layer
        classifier.add(Dense(units = 4, activation = 'relu'))
    # Adding the output layer
        classifier.add(Dense(units = 1, activation = 'sigmoid'))
    # Compiling the ANN
        classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
        
        return classifier
#---------------------------------------------------------------------------
  
    
    classifier = create_network()
    classifier.fit(X_train, y_train, batch_size = 25, epochs = 500)
  
    y_pred = classifier.predict(X_test)
    y_pred = (y_pred>0.5)
  
    
    cm = confusion_matrix(y_test, y_pred)
    acc = accuracy_score(y_test,y_pred)
    scores = classifier.evaluate(X_test,y_test)
 
    print(cm)
    print(acc)
    print(scores)
#---------------------------------------------------------------------------
    
    
    # Model Accuracy: how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
  
    # Model Precision: what percentage of positive tuples are labeled as such?
    print("Precision:",metrics.precision_score(y_test, y_pred))
    
    # Model Recall: what percentage of positive tuples are labelled as such?
    print("Recall:",metrics.recall_score(y_test, y_pred))
   
#---------------------------------------------------------------------------
    ann_viz(classifier, title="Neural Network for Diabetes Dataset")
#---------------------------------------------------------------------------
    
    
   









