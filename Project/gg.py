from collections import defaultdict
import sys
from scipy.stats import kendalltau
# This class represents a directed graph
# using adjacency list representation
class Graph:
    # Constructor
    def __init__(self, input_file):
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        self.shortest_paths = {}
        self.Rkryf_dict = {}
        self.Rkryf = []
        self.Rdioik_dict = {}
        self.Rdioik = []
        self.kendalRank = 0
        with open(input_file, 'r') as file:
            for line in file:
                nodes = line.strip().split(',')
                node1, node2 = map(int, nodes)
                self.addEdge(node1,node2)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        start = s
        # Create a queue for BFS
        queue = []
        shortest_paths = {(start,start) : [start]}
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:

                    shortest_paths[(start,i)] = shortest_paths[(start,s)] + [i]
                    queue.append(i)
                    visited[i] = True
        self.shortest_paths.update(shortest_paths)

    def NumberinPaths(self):
        Rkryf_dict = {}
        for paths in self.shortest_paths.values():
                for node in paths:
                    if node in Rkryf_dict:
                        Rkryf_dict[node] += 1/2
                    else:
                        Rkryf_dict[node] = 0

        self.Rkryf_dict.update(Rkryf_dict)

    def sortRkryf(self):
        self.Rkryf =  sorted(self.Rkryf_dict,key=lambda k: self.Rkryf_dict[k],reverse=True)

    def kendal(self):
        n = len(self.Rkryf)
        self.Rdioik = [3,4,5,2,1]
        discordant_pairs = []
        for i in range(n):
            for j in range(n):
                if i < j:
                    item11 = self.Rkryf[i]
                    item12 = self.Rkryf[j]
                    item21 = self.Rdioik[i]
                    item22 = self.Rdioik[j]
                    if (item11 < item12) and (item22 < item21):
                        if (item11, item12) not in discordant_pairs and (item12, item11) not in discordant_pairs:
                            discordant_pairs.append((item11, item12))
        self.kendalRank = 1 - (2 * len(discordant_pairs)) / ((n * (n - 1)) / 2)
        print(kendalltau(self.Rkryf,self.Rdioik))
        print(discordant_pairs)

# Driver code
if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = Graph(input_file = sys.argv[1])
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    for i in range(1, max(g.graph)+1):
        g.BFS(i)
    g.NumberinPaths()
    g.sortRkryf()
    g.kendal()
    print(g.kendalRank)