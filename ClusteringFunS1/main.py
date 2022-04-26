import random

header = ["height(cm)", "weight(kg)", "size(t-shirt)"]
table = [
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

def perform_k_means_clustering(table, k):
    # how to represent clusters? a few ways...
    # 1. a list of instances, 1 list per cluster
    # 2. add a column to the table for the cluster number
    # I recommend #2 because it is close to how sci kit
    # learn's KMeans algorithm works and you can use group by :)
    table = [row + [None] for row in table]

    # step 2
    random_instances = random.sample(table, k) # without replacement
    print(random_instances)
    for i in range(len(random_instances)):
        random_instances[i][-1] = i
    for row in table:
        print(row)

    # step 3
    # cluster_centers = compute_cluster_centroids(table, k)
    # for instance in table:
    #    nearest_cluster_num = find_nearest_cluster(instance, cluster_centers)
    #    update instances's cluster num

    # step 4
    # new_cluster_centers = compute_cluster_centroids(table, k)

    # step 5
    # moved = check_clusters_moved(cluster_centers, new_cluster_centers)
    # while moved .... repeat steps #3-4

    # goal is to return two lists
    # list of cluster numbers (labels_)
    # list of centroids (cluster_centers_)
    return [], [] # TODO: fix this

random.seed(0)
# step 1
k = 2
labels_, cluster_centers_ = perform_k_means_clustering(table, k)
print("cluster numbers:", labels_)
print("centroids:", cluster_centers_)