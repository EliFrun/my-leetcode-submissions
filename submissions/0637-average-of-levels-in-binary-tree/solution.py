# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        curr = [root]
        nextLayer = []
        ret = []
        
        while curr:
            layerSum = 0
            for node in curr:
                layerSum += node.val
                node.left and nextLayer.append(node.left)
                node.right and nextLayer.append(node.right)
                
            ret.append(layerSum/len(curr))
            curr = nextLayer
            nextLayer = []
            
            
        return ret
