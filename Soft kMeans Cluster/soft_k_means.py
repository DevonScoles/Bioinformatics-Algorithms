import numpy as np

def soft_kmeans(clusters,dimensions,softness,points,N=1,center=None):
    def distance(point,point1):
        return np.sqrt(sum((point[i]-point1[i])**2 for i in range (dimensions)))
    @np.vectorize
    def hidden_matrix(i,j):
        return np.exp(-softness*distance(center[i],points[j]))
    def step(center):
        clusterArray=np.array(range(clusters))
        pointsArray=np.array(range((len(points))))
        cc,pp=np.meshgrid(pointsArray,clusterArray,indexing='xy')
        n=hidden_matrix(pp,cc)
        d=np.sum(n,axis=0)
        matrix=np.divide(n,d)
        new_center=[[] for i in range(clusters)]
        for i in range(clusters):
            for j in range(dimensions):
                x_i_j=sum(matrix[i,l]*points[l][j] for l in range(len(points)))/sum(matrix[i,l] for l in range(len(points)))
                new_center[i].append(x_i_j)
        return new_center

    if center==None:
        center=points[:clusters]
    for i in range(N):
        center=step(center)
    return center

if __name__=='__main__':
    dimensions = -1
    clusters = -1
    softness = -1
    pointList=[]

    with open (r'Soft kMeans Cluster/rosalind_ba8d.txt') as f:

        for line in f:
            if clusters==-1:
                nums=line.strip().split()
                clusters=int(nums[0])
                dimensions=int(nums[1])
            elif softness==-1:
                softness=float(line.strip())
            else:
                pointList.append([float(v) for v in line.strip().split()])
        for pt in soft_kmeans(clusters,dimensions,softness,pointList,N=100):
            print (' '.join('{0:.3f}'.format(p) for p in pt))