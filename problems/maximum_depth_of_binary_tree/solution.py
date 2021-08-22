# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        visiting = [root]
        to_visit = []
        ret = []
        layer = -1
        while visiting:
            layer += 1
            lis = []
            for n in visiting:
                if n:
                    to_visit.append(n.left)
                    to_visit.append(n.right)
            visiting = to_visit
            to_visit = []
            
        return layer