# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def deepestLeavesSum(self, root: TreeNode) -> int:     
        current_layer = [root]
        next_layer = [root]
        sum = 0
        while len(next_layer) > 0:
            next_layer = []
            for node in current_layer:
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)
            if len(next_layer) > 0:
                current_layer = next_layer
                
        for node in current_layer:
            sum += node.val
        
        
        return sum
                
    

