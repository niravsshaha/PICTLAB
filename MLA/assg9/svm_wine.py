
# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.decomposition import PCA




# Importing the dataset
dataset = pd.read_csv('wine.data')
dataset.columns=["Class","Alcohol","Malic_acid","Ash","Alcalinity_of_ash","Magnesium","Total_phenols","Flavanoids","Nonflavanoid_phenols","Proanthocyanins","Color_intensity","Hue","OD280","Proline"] 
dataset.Class = dataset.Class-1


Y = dataset.iloc[:,0]


pca = PCA(n_components=2)
pca_x=pca.fit_transform(dataset.iloc[:,1:14])
X = pd.DataFrame(data=pca_x,columns=['comp1','comp2'])

# Splitting the dataset into the Training set and Test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)


# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Fitting SVM to the Training set
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, Y_train)


# Predicting the Test set results
Y_pred = classifier.predict(X_test)


# Making the Confusion Matrix
cm=confusion_matrix(Y_test, Y_pred)


accuracy_score(Y_test,Y_pred)
accuracy = (cm[0,0] + cm[1,1]) / (cm[0,0] + cm[0,1]+cm[1,0]+cm[1,1])  # Finding the accuracy of the model
accuracy



def wine(comp1,comp2):
    
    
    if(classifier.predict([[comp1,comp2]])==0):
        print("Class 1")
    elif (classifier.predict([[comp1,comp2]])==1):
        print("Class 2")
    else:
        print("Class 3")



wine(-0.17,0.99)


# Visualising the Training set results



