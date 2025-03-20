# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        a = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            a.append(node.val)
            inorder(node.right)

        inorder(root)

        queries = sorted(list(enumerate(queries)), key=lambda x: (x[1], x[0]))
        left = -1
        curr = 0
        right = a[curr]
        res = [None] * len(queries)
        for i,q in queries:
            if q < right:
                res[i] = [left, right]
            elif q == right:
                left = q
                right = q
                res[i] = [left, right]
            else:
                while curr < len(a) and a[curr] < q:
                    curr += 1
                left = a[curr - 1]
                right = a[curr] if curr < len(a) else -1
                if right == q:
                    left = right
                res[i] = [left, right]
        
        return res
        
