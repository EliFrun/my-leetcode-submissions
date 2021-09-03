"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        d = {}
        visiting = [node]
        to_visit = []
        
        while visiting:
            for n in visiting:
                if n.val not in d:
                    d[n.val] = [x.val for x in n.neighbors]
                for neighbor in n.neighbors:
                    if neighbor.val not in d:
                        to_visit.append(neighbor)
                        
            visiting = to_visit
            to_visit = []
                       

        new_nodes = {}
        
        for key, value in d.items():
            a = None
            if key not in new_nodes:
                a = Node(key)
                new_nodes[key] = a
            else:
                a = new_nodes[key]
                
            for v in value:
                b = None
                if v not in new_nodes:
                    b = Node(v)
                else:
                    b = new_nodes[v]
                a.neighbors.append(b)
                new_nodes[v] = b
         

        return new_nodes[node.val]
        
        
