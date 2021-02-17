# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return
            
        cur = len(preorder)
        for i in range(len(preorder)):
            if preorder[0] < preorder[i]:
                cur = i
                break
        
        return TreeNode(
            preorder[0],
            self.bstFromPreorder(preorder[1:cur]),
            self.bstFromPreorder(preorder[cur: ])
        )
