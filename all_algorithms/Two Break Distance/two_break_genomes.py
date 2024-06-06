class TwoBreakDist:
    def __init__(self):
        genomes = self.readin()
        distance = self.break_distance(genomes[0], genomes[1])
        print(distance)

    def cycle_chrome(self, nodes):
        length = len(nodes) // 2
        chrome = [0]*length
        for y in range(length):
            if nodes[2*y] < nodes[2*y+1]:
                chrome[y] = nodes[2*y+1]//2
            else:
                chrome[y] = -nodes[2*y]//2
        return chrome
    
    def chrome_cycle(self, chrome):
        length = len(chrome)
        nodes = [0]*(2*length)
        for y in range(length):
            x = chrome[y]
            if x > 0:
                nodes[2*y] = 2*x-1
                nodes[2*y+1] = 2*x
            else:
                nodes[2*y] = -2*x
                nodes[2*y+1] = -2*x-1
        return nodes
        

    def edges(self, genome):
        edges = set()
        for chrome in genome:
            nodes = self.chrome_cycle(chrome)
            nodes.append(nodes[0])
            for y in range(len(chrome)):
                edges.add((nodes[2*y+1], nodes[2*y+2]))
        return edges
        
    def break_distance(self, P, Q):
        parent = dict()
        rank = dict()
        blocks = sum([len(a) for a in P])
        edges = self.edges(P).union(self.edges(Q))

        for edge in edges:
            parent[edge[0]] = edge[0]
            parent[edge[1]] = edge[1]
            rank[edge[0]] = 0
            rank[edge[1]] = 0

        def get_parent(i):
            if i != parent[i]:
                parent[i] = get_parent(parent[i])
            return parent[i]
        
        def union(i, j):
            x = get_parent(i)
            y = get_parent(j)
            if x == y:
                return
            if rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[x] = y
                if rank[x] == rank[y]:
                    rank[y] += 1
        for edge in edges:
            union(edge[0], edge[1])
        sets = set()
        for edge in edges:
            id = get_parent(edge[0])
            sets.add(id)  
        cyclength = len(sets)
        distance = blocks - cyclength
        return distance
    
    def readin(self):
        with open("Two Break Distance/rosalind_ba6c.txt", 'r') as file:
            data = file.read().strip().split('\n')
        genomes = []
        for genome in data:
            genome = genome.split(')(')
            genomeLst = []
            for ch in genome:
                ch = ch.split()
                if ch[0][-1] != ')':
                    genomeLst.append([int(ch[0][1:] if '('==ch[0][0] else ch[0])] + [int(e) for e in ch[1:-1]] +\
                    [int(ch[-1][:-1] if ')'==ch[-1][-1] else ch[-1])])
                else:
                    genomeLst.append([int(ch[0][:-1])])
            genomes.append(genomeLst)
        return genomes

if __name__ == "__main__":
    TwoBreakDist()