import sys
import numpy as np

class NeighborJoining:
    def __init__(self):
        n, disMatrix = self.read_file()
        adj = self.neighbor_join(disMatrix, n)
        self.graph(adj)
        self.output(adj) 
        
    def format_input(self):
        data = sys.stdin.read().strip().split('\n')
        n = int(data[0])
        distanceMat = [[0]*n for _ in range(n)]
        for i in range(n):
            d = data[i+1].split()
            for k in range(n):
                distanceMat[i][k] = int(d[k])
        return n, distanceMat
    
    def read_file(self):
        f = open('NeighborJoining/test_input.txt', 'r')
        data = []
        for line in f:
            data.append(line.strip())
        n = int(data[0])
        distanceMat = [[0]*n for _ in range(n)]
        for i in range(n):
            d = data[i+1].split()
            for k in range(n):
                distanceMat[i][k] = int(d[k])
        return n, distanceMat

    def output(self, adj):
        file = open('NeighborJoining/out.txt', 'w')
        for i, lines in enumerate(adj):
            for d, w in lines:
                file.write(str(i)+'->'+str(d)+':'+'%0.3f' % w+'\n')

    def graph(self, adj):
        for i, lines in enumerate(adj):
            for d, w in lines:
                print(str(i)+'->'+str(d)+':'+'%0.3f' % w)

    def neighbor_join(self, disMatrix, n):
        distArray = np.array(disMatrix, dtype = float)
        leaves = [i for i in range(n)]
        adj = [[] for i in range(n)]
        if len(distArray) <= 1:
            return adj
        while True:
            if 2 == n:
                adj[len(adj)-1].append((len(adj)-2, distArray[0][1]))
                adj[len(adj)-2].append((len(adj)-1, distArray[0][1]))
                break
            totalDist = np.sum(distArray, axis = 0)
            D1 = (n-2) * distArray
            D1 = D1 - totalDist
            D1 = D1 - totalDist.reshape((n, 1))
            np.fill_diagonal(D1, 0.)
            index = np.argmin(D1)
            i = index // n
            j = index % n
            delta = (totalDist[i] - totalDist[j])/(n-2)
            li = (distArray[i, j]+delta)/2
            lj = (distArray[i, j]-delta)/2
            d_new = (distArray[i, :]+distArray[j, :]-distArray[i, j])/2
            distArray = np.insert(distArray, n, d_new, axis = 0)
            d_new = np.insert(d_new, n, 0., axis = 0)
            distArray = np.insert(distArray, n, d_new, axis = 1)
            distArray = np.delete(distArray, [i, j], 0)
            distArray = np.delete(distArray, [i, j], 1)

            m = len(adj)
            adj.append([])
            adj[m].append((leaves[i], li))
            adj[leaves[i]].append((m, li))
            adj[m].append((leaves[j], lj))
            adj[leaves[j]].append((m, lj))
            if i < j:
                del leaves[j]
                del leaves[i]
            else:
                del leaves[i]
                del leaves[j]
            leaves.append(m)
            n -= 1
        return adj

if __name__ == "__main__":
    NeighborJoining()
