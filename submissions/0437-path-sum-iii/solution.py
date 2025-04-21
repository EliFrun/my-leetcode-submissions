# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ret = 0
        def dfs(lis, node):
            nonlocal ret
            if not node:
                return
            for i in range(len(lis)):
                lis[i] += node.val
            
            lis.append(node.val)
            ret += sum([1 if x == targetSum else 0 for x in lis])
            dfs(lis, node.left)
            dfs(lis, node.right)
            lis.pop()
            for i in range(len(lis)):
                lis[i] -= node.val

        dfs([], root)
        return ret
        
