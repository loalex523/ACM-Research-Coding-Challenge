# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.


Alex Lo
9/8/2020

LIBRARIES USED: 
- Pandas
- Numpy
- Sklearn.cluster => KMeans

CITED SOURCES: 
https://heartbeat.fritz.ai/k-means-clustering-using-sklearn-and-python-4a054d67b187

Explanation of my attempt: 
To calculate the number of optimal clusters in the data set, I first had to understand how clustering algorithms work. In Python, there are many clustering algorithms such as affinity propogation, mean shift, and many others. The clustering algorithm I chose was KMeans simply due to its widely known usage as well as the ability to modify the number of clusters that I wanted to find through the parameters. I did some more research on the KMeans algorithm and discovered the elbow method. This helps discover the optimal n clusters for the dataset by observing the 'elbow' part of the graph where the line would flatten out. 

To solve the problem, I first used the Pandas library in Python to prettify the data and arrange it in floating numbers. Once I arranged my data, I used the KMeans function from the kmeans library to enact the KMeans algorithm. Since I was working with a small set of data I decided the amount of clusters could not amass to more than 10, so I used a for loop to loop through the kmeans datapoints and append it to the array. Finally, I used the pyplot library to plot my data points and carefully observed the change in slope to determine my answer of 3.
