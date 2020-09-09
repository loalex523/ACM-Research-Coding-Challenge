import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import csv 

#Read in the csv
db = pd.read_csv('ClusterPlot.csv')

#Collect the V1 and V2 rows of the .csv sheet
data = db.iloc[:, [1,2]].values
#Print test data to make sure format is right
print(data)

#Holds datapoints in kmeans.
datapoints = [] 

#finds number of optimal clusters the dataset should have based off the KMeans from ranges 1 to 15
for i in range(1, 4):
    kmeans = KMeans(n_clusters=i).fit(data)
    kmeans.fit(data)
    datapoints.append(kmeans.inertia_)

#Plot points using elbow method
plt.plot(range(1,4), datapoints)
plt.show()