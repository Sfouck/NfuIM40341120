from lib.clustering import *

if __name__ == "__main__":

    inputs = [[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],[-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],[-41,8],[-11,-6],[-25,-9],[-18,-3]]

    random.seed(0) # so you get the same results as me
    clusterer = KMeans(3)
    clusterer.train(inputs)
    print "3-means:"
    print clusterer.means
    print

    random.seed(0)
    clusterer = KMeans(2)
    clusterer.train(inputs)
    print "2-means:"
    print clusterer.means
    print

    print "errors as a function of k"

    for k in range(1, len(inputs) + 1):
        print k, squared_clustering_errors(inputs, k)
    print

    img_path = "data/flower.png"
    recolor_image(img_path,3)
    recolor_image(img_path,5)

    print "bottom up hierarchical clustering"

    base_cluster = bottom_up_cluster(inputs)
    print base_cluster

    print
    print "three clusters, min:"
    for cluster in generate_clusters(base_cluster, 3):
        print get_values(cluster)

    print
    print "three clusters, max:"
    base_cluster = bottom_up_cluster(inputs, max)
    for cluster in generate_clusters(base_cluster, 3):
        print get_values(cluster)