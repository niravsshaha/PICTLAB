


import numpy as np		
import pandas as pd
import matplotlib.pyplot as plt     # For plotting graph
%matplotlib inline		       # For display ploted graph

from sklearn import datasets	       # Import inbuilt datasets
from sklearn.cluster import KMeans    # To use inbuilt k-means function for calculating k-means
from sklearn.metrics import accuracy_score    # To display accuracy score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

dataset = pd.read_csv("wine.data")

dataset.columns=["Class","Alcohol","Malic_acid","Ash","Alcalinity_of_ash","Magnesium","Total_phenols","Flavanoids","Nonflavanoid_phenols","Proanthocyanins","Color_intensity","Hue","OD280","Proline"] 
df = pd.DataFrame(dataset)
df.head() 


dataset['Class']=dataset['Class'].replace(3,0)
dataset['Class']=dataset['Class'].replace(1,3)
dataset['Class']=dataset['Class'].replace(2,1)
dataset['Class']=dataset['Class'].replace(3,2)


target = dataset['Class']    

df=df.iloc[0:177,[1,12]]


sc=StandardScaler()
df=sc.fit_transform(df)

pca = PCA(n_components=2)
pca_x=pca.fit_transform(df)
pca_df = pd.DataFrame(data=pca_x,columns=['comp1','comp2'])


KModel = KMeans(n_clusters=3,random_state=2)
KModel.fit_predict(pca_df)
KModel.labels_


colormap = np.array(['Red','Blue','Green'])


z = plt.scatter(pca_df.comp1,pca_df.comp2,c = colormap[KModel.labels_])
KModel.labels_
accuracy_score(target,KModel.labels_)




