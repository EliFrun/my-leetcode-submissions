# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(lambda: defaultdict(list))
        def solve(node, idx, layer):
            if not node:
                return
            d[idx][layer].append(node.val)
            solve(node.left, idx - 1, layer + 1)
            solve(node.right, idx + 1, layer + 1)
        
        solve(root, 0, 0)
        ret = []
        for k in sorted(d.keys()):
            l = []
            for layer in sorted(d[k].keys()):
                l += sorted(d[k][layer])
            ret.append(l)
        return ret
