# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        def d(f):
            if not f:
                return -1
            return 1 + d(f.left)
        
        depth = d(root)
        if depth == 0:
            return 1
        
        bottom = 2 ** (depth) 
        top = 2 ** (depth + 1) - 1
        
        def exists(n, s):
            if not n:
                return False
            if not s:
                return True if n else False
            return exists(n.left, s[1:]) if s[0] == "0" else exists(n.right, s[1:])
        
        
        while top - bottom > 1:
            mid = (top + bottom) // 2
            if exists(root, bin(mid)[3:]):
                bottom = mid
            else:
                top = mid
        
                
        return top if exists(root, bin(top)[3:]) else bottom
        
        
