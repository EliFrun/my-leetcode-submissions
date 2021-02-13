# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.inline_traversal(cloned, target.val)
        
        
    def inline_traversal(self, cur: TreeNode, value: int) -> TreeNode:
        if cur is None:
            return
        if cur.val == value:
            return cur
        

        return self.inline_traversal(cur.left, value) or self.inline_traversal(cur.right, value)  
