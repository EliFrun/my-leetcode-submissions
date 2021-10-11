# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(n, m):
            if not n:
                return 0
            return (1 if n.val >= m else 0) + traverse(n.left, max(m, n.val)) + traverse(n.right, max(m, n.val))
        
        return traverse(root, root.val)
