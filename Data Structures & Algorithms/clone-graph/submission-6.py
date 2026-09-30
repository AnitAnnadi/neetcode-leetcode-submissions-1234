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

        nodes = {}
        def cloneGraphHelper(node):
            copy = Node(node.val)
            nodes[node] = copy

            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    cloneGraphHelper(neighbor)

                copy.neighbors.append(nodes[neighbor])

        cloneGraphHelper(node)
        return nodes[node]
                

