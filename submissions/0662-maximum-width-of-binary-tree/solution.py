# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        current_layer = [(root,1)]
        max_layer = 0
        while(1):
            next_layer = []
            while(current_layer and current_layer[0][0] is None):
                current_layer.pop(0)

            while(current_layer and current_layer[-1][0] is None):
                current_layer.pop(-1)
                

            for node in current_layer:
                if node[0] is not None:
                    next_layer.append((node[0].left, 1))
                    next_layer.append((node[0].right, 1))
                else:
                    next_layer.append((None, 2*node[1]))
                    
                
            current_width = sum([i[1] for i in current_layer])
            max_layer = max(max_layer, current_width)
            if not current_layer:
                return max_layer
            
            
            current_layer = next_layer
            next_layer = []
            
        
