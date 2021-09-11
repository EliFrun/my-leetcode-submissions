# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        curr = [root]
        foo = []
        ret = []
        while curr:
            for n in curr:
                if n:
                    n.left and foo.append(n.left)
                    n.right and foo.append(n.right)
            
            ret.append(curr[-1].val)
            curr = foo
            foo = []
            
        return ret
        
