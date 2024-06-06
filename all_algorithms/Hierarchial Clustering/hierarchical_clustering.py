def hierarchical_clustering(dist_mat, method='Davg'):
    clusters = [[i] for i in range(len(dist_mat))]

    lst = []
    while len(clusters) > 1:
        minimum_dist = float('inf')
        for i in range(len(clusters) - 1):
            for j in range(i + 1, len(clusters)):
                if method == 'Davg':
                    dist = 0
                    for x in clusters[i]:
                        for x1 in clusters[j]:
                            dist += dist_mat[x][x1]
                    dist /= (len(clusters[i]) * len(clusters[j]))

                if dist < minimum_dist:
                    minimum_dist = dist
                    nearest_x = i
                    nearest_x1 = j

        new_cluster = clusters[nearest_x] + clusters[nearest_x1]
        clusters = [clu for clu in clusters if clu not in [clusters[nearest_x], clusters[nearest_x1]]]
        clusters.append(new_cluster)
        lst.append(new_cluster)
    return lst

if __name__ == "__main__":
    file = open("Hierarchial Clustering/test_input.txt",'r')
    data = file.read().splitlines()
    n = int(data[0])
    dist_mat = []
    for i in range(1, len(data)):
        dist_mat.append([float(d) for d in data[i].split(' ')])
    lst = hierarchical_clustering(dist_mat, 'Davg')
    for clust in lst:
        print(' '.join([str(x + 1) for x in clust]))
