# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        curr = [root]
        
        while curr:
            next_row = []
            for node in curr:
                node.left and next_row.append(node.left)
                node.right and next_row.append(node.right)
                
            ret.append(max(x.val for x in curr))
            curr = next_row
            
        return ret
