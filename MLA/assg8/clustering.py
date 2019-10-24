# Importing necessary Packages
import numpy as np		
import pandas as pd
import matplotlib.pyplot as plt     # For plotting graph
%matplotlib inline		       # For display ploted graph
from sklearn import datasets	       # Import inbuilt datasets
from sklearn.cluster import Kmeans    # To use inbuilt k-means function for calculating k-means
from sklearn.metrics import accuracy_score    # To display accuracy score

# Load iris dataset from avilable datasets
iris = datasets.load_iris()

# Convert iris dataset into pandas DataFrame
x = pd.DataFrame(iris.data)

# Output of converted data
x.head()



# Giving names to columns
x.columns= ['sepal_length','sepal_width','petal_length','petal_width']

# Now dataset is
x.head();

# Now apply k-means algorithm on iris dataset with 3 clusters as in iris dataset we have target value as species with 3 values as Setosa, Virginica, Versicolor
a = Kmeans(n_clusters=3)

# Fit k-means algorithm on iris dataset
a.fit(x)

# Assign labels to target
#a.labels_

# Giving color to target variable
colormap = np.array(['Red','Blue','Green'])

# Plot clusters on scatter plot
z = plt.scatter(x.sepal_length,x.sepal_width,x.petal_length,c = colormap[a.labels_])

# Find out accuracy score
accuracy_score(iris.target,a.labels_)
    # Accuracy score of k-means algorithm on iris dataset
