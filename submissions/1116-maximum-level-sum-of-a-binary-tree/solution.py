# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr = [root]
        layer = 1
        m = float('-inf')
        ret = 0
        while curr:
            v = sum([x.val for x in curr]) 
            if v > m:
                m = v
                ret = layer  
            
            nxt = []
            for node in curr:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            
            curr = nxt
            layer += 1

        return ret
        
