# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        nums = inorder(root) + [val]
        def solve(lis):
            if not lis:
                return None
            return TreeNode(
                max(lis),
                solve(lis[:lis.index(max(lis))]),
                solve(lis[lis.index(max(lis)) + 1:])
            )

        return solve(nums)

                    
