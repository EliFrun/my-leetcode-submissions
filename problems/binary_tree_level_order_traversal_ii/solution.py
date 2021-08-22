# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        visiting = [root]
        to_visit = []
        ret = []
        while visiting:
            lis = []
            for n in visiting:
                if n:
                    to_visit.append(n.left)
                    to_visit.append(n.right)
                n and lis.append(n.val)
            ret = [lis] + ret if lis else ret
            visiting = to_visit
            to_visit = []
            
        return ret