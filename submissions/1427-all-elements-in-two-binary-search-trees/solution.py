# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        curr = [root1, root2]
        visited = set()

        while curr:
            nxt = set()
            for node in curr:
                if not node:
                    continue
                visited.add(node)
                nxt.add(node.left)
                nxt.add(node.right)

            curr = nxt

        return sorted([x.val for x in visited])
