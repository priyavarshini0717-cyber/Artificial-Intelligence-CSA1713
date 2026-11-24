import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
X = np.array([
    [1, 2],
    [1, 4],
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
])

kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
kmeans.fit(X)

labels = kmeans.labels_

print("Cluster Labels:")
print(labels)

print("\nCluster Centers:")
print(kmeans.cluster_centers_)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    color='red',
    marker='X',
    s=200,
    label='Centroids'
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
