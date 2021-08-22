# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visiting = [root]
        to_visit = []
        ret = []
        layer = 0
        while visiting:
            lis = []
            for n in visiting:
                if n:
                    to_visit.append(n.left)
                    to_visit.append(n.right)
                n and lis.append(n.val)
            lis and (ret.append(lis) if layer % 2 == 0 else ret.append(reversed(lis)))
            visiting = to_visit
            to_visit = []
            layer += 1
            
        return ret
