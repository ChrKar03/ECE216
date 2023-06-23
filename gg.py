from collections import defaultdict
import sys

# This class represents a directed graph
# using adjacency list representation
class Graph:
    # Constructor
    def __init__(self, input_file):
        # Default dictionary to store graph
        self.graph = defaultdict(list)
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
 
        # Create a queue for BFS
        queue = []
        shortest_paths = {s : [s]}
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
                    shortest_paths[i] = shortest_paths[s] + [i]
                    queue.append(i)
                    visited[i] = True
        print(shortest_paths)
# Driver code
if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = Graph(input_file = sys.argv[1])
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)