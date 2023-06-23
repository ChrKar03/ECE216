from collections import defaultdict
import sys

# This class represents a directed graph
# using adjacency list representation
class Graph:
    # Constructor
    def __init__(self, input_file):
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        self.shortest_paths = {}
        self.Rkryf = {}
        self.Rkyfkeys = []
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
        Rkryf = {}
        for paths in self.shortest_paths.values():
                for node in paths:
                    if node in Rkryf:
                        Rkryf[node] += 1/2
                    else:
                        Rkryf[node] = 0

        self.Rkryf.update(Rkryf)

    def sortRkryf(self):
        self.Rkyfkeys =  sorted(self.Rkryf,key=lambda k: self.Rkryf[k],reverse=True)


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
    print(g.Rkyfkeys)