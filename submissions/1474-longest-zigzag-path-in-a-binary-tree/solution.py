# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def zig(depth, node):
            nonlocal ret
            if node == None:
                ret = max(ret, depth - 1)
                return

            zag(depth + 1, node.right)
            zig(1, node.left)

        def zag(depth, node):
            nonlocal ret
            if node == None:
                ret = max(ret, depth - 1)
                return
            
            zig(depth + 1, node.left)
            zag(1, node.right)

        zig(0, root)
        zag(0, root)
        
        return ret
