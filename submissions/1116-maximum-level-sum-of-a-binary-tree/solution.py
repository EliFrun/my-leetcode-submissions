# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr = [root]
        layer = 1
        ret = 1
        best = root.val
        while curr and any(curr):
            nxt = []
            s = sum([x.val for x in curr if x])
            if s > best:
                ret = layer
                best = s

            for n in curr:
                if not n:
                    continue
                nxt.append(n.left)
                nxt.append(n.right)
            layer += 1
            curr = nxt
        return ret
            
