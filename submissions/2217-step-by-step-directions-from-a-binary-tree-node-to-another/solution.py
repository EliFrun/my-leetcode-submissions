# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        g = defaultdict(set)
        def dfs(curr, parent):
            if parent:
                g[curr.val].add((parent.val, 'U'))
            if curr.left:
                g[curr.val].add((curr.left.val, 'L'))
                dfs(curr.left, curr)
            if curr.right:
                g[curr.val].add((curr.right.val, 'R'))
                dfs(curr.right, curr)

        dfs(root, None)

        enabled = defaultdict(lambda:True)
        def pathfind(curr, target):
            if curr == target:
                return '+'
            ret = ""
            enabled[curr] = False
            for n, d in g[curr]:
                if not enabled[n]:
                    continue
                if (v := pathfind(n, target)):
                    ret = d + v
                    break
            enabled[curr] = True

            return ret

        return pathfind(startValue, destValue)[:-1]


        

        
