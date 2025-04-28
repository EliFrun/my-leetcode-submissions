# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        curr = []
        if root:
            curr.append(root)
        lis = []
        while curr:
            lis.append(max(x.val for x in curr))
            nxt = []
            for n in curr:
                if n.left:
                    nxt.append(n.left)
                if n.right:
                    nxt.append(n.right)
                    
            curr = nxt
            
        return lis
            
        
