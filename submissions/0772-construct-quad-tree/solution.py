"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(gr):
            if len(gr) == 1:
                return Node(gr[0][0], True)
            node = Node()
            node.topLeft = build([gr[i][:len(gr[i])//2] for i in range(len(gr)//2)])
            node.topRight = build([gr[i][len(gr[i])//2:] for i in range(len(gr)//2)])
            node.bottomLeft = build([gr[i][:len(gr[i])//2] for i in range(len(gr)//2, len(gr))])
            node.bottomRight = build([gr[i][len(gr[i])//2:] for i in range(len(gr)//2, len(gr))])
            if node.topLeft.val != -1 and all([x.val == node.topLeft.val for x in [node.topLeft, node.topRight, node.bottomLeft, node.bottomRight]]):
                node.val = node.topLeft.val
                node.isLeaf = True
                node.topLeft = None
                node.topRight = None
                node.bottomLeft = None
                node.bottomRight = None
            else:
                node.val = -1
                node.isLeaf = False
            return node

        return build(grid)
        
