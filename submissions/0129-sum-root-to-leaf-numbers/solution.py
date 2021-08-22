# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        allnums = self.allpaths(root)
        
        total = 0
        for a in allnums:
            curr = 0
            for i in enumerate(reversed(a)):
                curr += int(i[1] * (10 ** i[0]))
            
            total += curr
                
        return total
        
        
    def allpaths(self, root):
        if not root:
            return []
        
        if not root.left and not root.right:
            return [[root.val]]
        
        return [
            [root.val] + x for x in self.allpaths(root.left) + self.allpaths(root.right)
        ]
