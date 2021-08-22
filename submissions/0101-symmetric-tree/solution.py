# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        current_layer = [(root.left, None) if root.left else (None, 1), (root.right, None) if root.right else (None, 1)]
        next_layer = []
        
        
        while any([x[0] for x in current_layer]):
            a = current_layer[0:len(current_layer)//2]
            b = reversed(current_layer[len(current_layer)//2:])
            for i,j in zip(a,b):
                if not i[0] and not j[0]:
                    if i[1] != j[1]:
                        return False
                elif i[0] and j[0]:
                    if i[0].val != j[0].val:
                        return False
                else:
                    return False
                
            for i in current_layer:
                if not i[0]:
                    next_layer.append((None, 2 * i[1]))
                else:
                    next_layer.append((i[0].left, None) if i[0].left else (None, 1))
                    next_layer.append((i[0].right, None) if i[0].right else (None, 1))
                     
            current_layer = next_layer
            next_layer = []
                    
            
        return True
