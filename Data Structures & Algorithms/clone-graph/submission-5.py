"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        graph = {}

        newNode = Node(node.val)
        graph[newNode.val] = newNode

        self.cloneGraphHelper(node, graph)

        return newNode


    def cloneGraphHelper(self, node, graph):
        
        for n in node.neighbors:
            if n.val not in graph:
                graph[n.val] = Node(n.val)
                self.cloneGraphHelper(n, graph)

            graph[node.val].neighbors.append(graph[n.val])