import math

# cf --> Closeness Factor

# distance between 2 points
def distance(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

# finds the cluster of points for given Closeness Factor(cf) in list of points for given point.
def cluster_find(point, points, cf):
    cluster = []
    cluster.append(point)
    for pt in points:
        if ( distance(point, pt) < cf) and (  point != pt ) :
            cluster.append(pt)
    return cluster


# Checks is there any common points in 2 clusters, if present return true.
def check_intersection(cluster1, cluster2):
    if len(list(set(cluster1) & set(cluster2))) > 0 :
        return True
    return False


def cluster_finder(point_list, cf):
    clusters = []
    flag = []
    remove_cluster = []
    for pt in point_list:
        clusters.append(cluster_find(pt, point_list, cf))
        flag.append(0)

    for i in range(len(clusters)):
        for j in range(len(clusters)):
            if i != j and (flag[i] == 0) and (flag[j] == 0):
                if check_intersection(clusters[i], clusters[j]):
                    clusters[i]  =  clusters[i] + clusters[j]
                    remove_cluster.append(clusters[j])
                    flag[j] =  1

    for cluster in  remove_cluster:
        clusters.remove(cluster)
    final_clusters = []
    for cluster in clusters:
        final_clusters.append(list(set(cluster)))
    return  final_clusters

def  circle_cluster():
    points = [(1,2,3), (2,3,4), (2,3,5), (10,10,10)]
    cf =  1
    print(cluster_finder(points, cf))


circle_cluster()
