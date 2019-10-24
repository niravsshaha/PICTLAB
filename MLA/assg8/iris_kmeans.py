
import numpy as np		
import pandas as pd
import matplotlib.pyplot as plt     # For plotting graph
%matplotlib inline		       # For display ploted graph

from sklearn import datasets	       # Import inbuilt datasets
from sklearn.cluster import KMeans    # To use inbuilt k-means function for calculating k-means
from sklearn.metrics import accuracy_score    # To display accuracy score


iris = datasets.load_iris()
df = pd.DataFrame(iris.data)
df.head()


df.columns= ['sepal_length','sepal_width','petal_length','petal_width']
df.head();


KModel = KMeans(n_clusters=3)
KModel.fit(df)

# Assign labels to target
#a.labels_


colormap = np.array(['Red','Blue','Green'])


z = plt.scatter(df.sepal_length,df.sepal_width,df.petal_length,c = colormap[KModel.labels_])
accuracy_score(iris.target,KModel.labels_)

    
    
    
