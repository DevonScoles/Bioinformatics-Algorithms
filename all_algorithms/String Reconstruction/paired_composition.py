import sys

class EulerianPath:
    def __init__(self, adjecencyLst):
        self.adjecencyLst = adjecencyLst
        self.updateAdjecencyLst()

    def updateAdjecencyLst(self):
        self.unexplored = dict()
        self.indegree = dict()
        self.outdegree = dict()
        self.adjecencyLstCurPos = dict()
        self.unbalanced = []
        self.path = []
        self.n = len(self.adjecencyLst)
        self.edges = 0 
        for _, vList in self.adjecencyLst.items():
            self.indegree[_] = self.indegree.get(_, 0)
            for v in vList:
                self.indegree[v] = self.indegree.get(v, 0) + 1
            l = len(vList)
            self.outdegree[_] = l
            self.edges += l
            self.adjecencyLstCurPos[_] = 0

    
    def addEdge(self):
        if type(self.adjecencyLst) is dict:
            for v in self.adjecencyLst.keys():
                if self.indegree[v] != self.outdegree[v]:
                    if self.indegree[v] < self.outdegree[v]:
                        self.unbalanced.append(v)
                    else:
                        self.unbalanced.insert(0, v)
            if len(self.unbalanced) > 0:
                self.adjecencyLst[self.unbalanced[0]].append(self.unbalanced[1])
                self.outdegree[self.unbalanced[0]] += 1
                self.indegree[self.unbalanced[1]] += 1
            return    
        for v in range(self.n):
            if self.indegree[v] != self.outdegree[v]:
                if self.indegree[v] < self.outdegree[v]:
                    self.unbalanced.append(v)
                else:
                    self.unbalanced.insert(0, v)
        if len(self.unbalanced) > 0:
            self.adjecencyLst[self.unbalanced[0]].append(self.unbalanced[1])
            self.outdegree[self.unbalanced[0]] += 1
            self.indegree[self.unbalanced[1]] += 1
        return
    
    def updatePath(self, start):
        l = len(self.path) - 1
        self.path = self.path[start:l] + self.path[:start]
        for node, pos in self.unexplored.items():
            if pos < start:
                self.unexplored[node] = pos + l - start
            else:
                self.unexplored[node] = pos - start
        return

    def exploreGraph(self, s):
        self.path.append(s)
        curPos = self.adjecencyLstCurPos[s]
        curMaxPos = self.outdegree[s]
        while curPos < curMaxPos:
            self.adjecencyLstCurPos[s] = curPos + 1
            if curPos + 1 < curMaxPos:
                self.unexplored[s] = len(self.path) - 1
            else:
                if s in self.unexplored:
                    del self.unexplored[s]
            v = self.adjecencyLst[s][curPos]
            self.path.append(v)
            s = v
            curPos = self.adjecencyLstCurPos[s]
            curMaxPos = self.outdegree[s]
            self.edges -= 1
        return

    def eulerianCycle(self):
        if type(self.adjecencyLst) is dict:
            w, vList = self.adjecencyLst.popitem()
            self.adjecencyLst[w] = vList
            self.exploreGraph(w)
        else:
            self.exploreGraph(0)
        while self.edges > 0:
            node, pos = self.unexplored.popitem()
            self.updatePath(pos)
            self.exploreGraph(node)
        return self.path
    
    def eulerianPath(self):
        self.addEdge()
        self.eulerianCycle()
        if len(self.unbalanced) > 0:
            for i in range(len(self.path)-1):
                if self.path[i] == self.unbalanced[0] and self.path[i+1] == self.unbalanced[1]:
                    self.updatePath(i+1)
                    break
        return self.path             


class PairedStringReconstruction:
    def __init__(self):
        self.k, self.d, self.adjecencyLst = self.readin()
        self.path = EulerianPath(self.adjecencyLst).eulerianPath()
        print(self.GapPat(self.path, self.k, self.d))       

    def readin(self):
        with open("String Reconstruction/rosalind_ba3j.txt", 'r') as file:
            data = file.read().strip().split()
        k, d = int(data[0]), int(data[1])
        patterns = [tuple(p.split('|')) for p in data[2:]]
        adjecencyLst = self.DeBrujin(k, patterns)
        return k, d, adjecencyLst

    def DeBrujin(self, k, patterns):
        debrudict = dict()
        for pattern in patterns:
            pl = tuple([pattern[0][:k-1], pattern[1][:k-1]])
            pr = tuple([pattern[0][1:], pattern[1][1:]])
            if pl in debrudict:
                debrudict[pl].append(pr)
            else:
                debrudict[pl] = []
                debrudict[pl].append(pr)
            if pr not in debrudict:
                debrudict[pr] = []
        return debrudict
    
    def GapPat(self, patterns, k, d):
        pat1 = patterns[0][0] + ''.join([p[0][-1] for p in patterns[1:]])
        pat2 = patterns[0][1] + ''.join([p[1][-1] for p in patterns[1:]])
        l = len(pat1)
        if pat1[k+d:] == pat2[:l-k-d]:
            return pat1 + pat2[-(k+d):]

if __name__ == "__main__":
    PairedStringReconstruction()