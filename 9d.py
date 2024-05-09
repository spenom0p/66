# Step 1: Import necessary libraries
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 2: Generate random data for demonstration
np.random.seed(42)
data = np.random.rand(100, 2)

# Step 3: Number of clusters (you can adjust this)
num_clusters = 3

# Step 4: Create KMeans instance
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# Step 5: Fit the data to the KMeans model
kmeans.fit(data)

# Step 6: Get the cluster assignments and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Step 7: Visualize the clusters
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', edgecolor='k')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, color='red')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
