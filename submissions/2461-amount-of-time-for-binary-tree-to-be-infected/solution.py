# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        def dfs(node):
            if not node:
                return False
            if node.val == start:
                l.append(node)
                return True
            if dfs(node.left):
                l.append(node)
                return True
            elif dfs(node.right):
                l.append(node)
                return True
            return False


        @cache
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        l = []
        dfs(root)
        l = l[::-1]
        ret = depth(l[-1]) - 1
        for i in range(len(l) - 1):
            v =  depth(l[i].left if l[i].right and l[i + 1].val == l[i].right.val else l[i].right)
            ret = max(ret, len(l) - i - 1 + v)

        return ret
            
            
        
