#Print adjacency lisT
from typing import List
class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(V)]
        
        for edge in edges:
            node1, node2 = edge
            adj[node1].append(node2)
            adj[node2].append(node1)
        return adj
