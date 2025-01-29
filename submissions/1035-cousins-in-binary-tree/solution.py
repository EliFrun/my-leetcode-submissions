# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        curr = [root]
        while curr:
            nxt = []
            found = []
            for c in curr:
                if c.val == x:
                    found.append(x)
                if c.val == y:
                    found.append(y)
                if c.left:
                    nxt.append(c.left)
                if c.right:
                    nxt.append(c.right)

                if c.left and c.left.val == x and c.right and c.right.val == y:
                    return False
                if c.left and c.left.val == y and c.right and c.right.val == x:
                    return False

            if len(found) == 1:
                return False
            if len(found) == 2:
                return True
            curr = nxt

        return False
        
