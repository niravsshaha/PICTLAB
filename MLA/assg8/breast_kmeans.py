

import numpy as np		
import pandas as pd
import matplotlib.pyplot as plt     # For plotting graph
%matplotlib inline		       # For display ploted graph

from sklearn import datasets	       # Import inbuilt datasets
from sklearn.cluster import KMeans    # To use inbuilt k-means function for calculating k-means
from sklearn.metrics import accuracy_score    # To display accuracy score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("breast.data",na_values = ['?'])
df = pd.DataFrame(dataset)
df.head()

df.columns=["Sample_code_number","Clump_Thickness","Uniformity_of_Cell_Size","Uniformity_of_Cell_Shape","Marginal_Adhesion","Single_Epithelial_Cell_Size","Bare_Nuclei","Bland_Chromatin","Normal_Nucleoli","Mitoses","Class"]


median = df['Bare_Nuclei'].median()
df['Bare_Nuclei'].fillna(median, inplace=True)  


df['Class']=df['Class'].replace(2,0)
df['Class']=df['Class'].replace(4,1)


target = df['Class']    


df=df.iloc[0:698,1:10]    #slicing data 


sc=StandardScaler()
x=sc.fit_transform(df)

pca = PCA(n_components=2)	
pca_x=pca.fit_transform(x)
pca_df = pd.DataFrame(data=pca_x,columns=['comp1','comp2'])


KModel = KMeans(n_clusters=2,random_state=2)
KModel.fit_predict(pca_df)
KModel.labels_             


colormap = np.array(['Red','Blue'])     


z = plt.scatter(pca_df.comp1,pca_df.comp2,c = colormap[KModel.labels_])
accuracy_score(target,KModel.labels_)






