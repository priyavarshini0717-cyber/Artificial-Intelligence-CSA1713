from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = [
    [2, 3, 5],
    [4, 6, 8],
    [6, 8, 10],
    [8, 10, 12],
    [10, 12, 15]
]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("PRINCIPAL COMPONENT ANALYSIS")
print("----------------------------")

print("Original Dataset:")
print(X)

print("\nOriginal Dimensions:", len(X[0]))

print("\nReduced Dataset:")
print(X_pca)

print("\nReduced Dimensions:", X_pca.shape[1])

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)
