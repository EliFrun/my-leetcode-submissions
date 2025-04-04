# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = set([root])
        deepest = None
        while curr:
            deepest = curr
            nxt = set()
            for n in curr:
                if n.left:
                    nxt.add(n.left)
                if n.right:
                    nxt.add(n.right)
            curr = nxt

        deepest = set([n.val for n in deepest])
        deep = None
        def dfs(n):
            nonlocal deep
            if not n:
                return set()
            ret = set([n.val])
            ret = ret.union(dfs(n.left))
            ret = ret.union(dfs(n.right))
            if not deep and ret.intersection(deepest) == deepest:
                deep = n

            return ret
        dfs(root)
        return deep
        
