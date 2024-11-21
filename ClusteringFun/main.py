

header = ["height(cm)", "weight(kg)"] #, "size(t-shirt)"]
X_train = [
    [158, 58], # "M"
    [158, 59], # "M"
    [158, 63], # "M"
    [160, 59], # "M"
    [160, 60], # "M"
    [163, 60], # "M"
    [163, 61], # "M"
    [160, 64], # "L"
    [163, 64], # "L"
    [165, 61], # "L"
    [165, 62], # "L"
    [165, 65], # "L"
    [168, 62], # "L"
    [168, 63], # "L"
    [168, 66], # "L"
    [170, 63], # "L"
    [170, 64], # "L"
    [170, 68] # "L"
]
# TODO: normalize data before calculating distances

# k-means clustering algorithm (a greedy algorithm)
# 1. Pick a k (e.g. k = 2)
# 2. Select k (random) instances for the initial cluster centroids (has an effect on the final resulting clusters… not guaranteed to find the "global" optimal solution, just a "local" optimal solution)
# 3. Assign each instance to the cluster with the “nearest” centroid
# 4. Re-calculate the centroids
# 5. Repeat steps #3-4 until the centroids no longer "move"