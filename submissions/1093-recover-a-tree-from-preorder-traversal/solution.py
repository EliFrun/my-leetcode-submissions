# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def solve(depth, st):
            #print(depth, st)
            if not st:
                return None
            curr = TreeNode(int(st[0]))
            start = [i for i,v in enumerate(st) if v == '-' * (depth + 1)]
            if len(start) == 0:
                start = len(st)
            elif len(start) == 1:
                start = len(st)
            else:
                start = start[-1]
            curr.left = solve(depth + 1, st[2:start])
            curr.right = solve(depth + 1, st[start + 1:])
            return curr
            


        t = []
        curr = ''
        for c in traversal:
            if c == '-':
                if curr and curr[-1] == c:
                    pass
                else:
                    t.append(curr)
                    curr = ''
            else:
                if curr and curr[-1] == '-':
                    t.append(curr)
                    curr = ''  
            curr += c
        t.append(curr)
        return solve(0, t)

            
            
