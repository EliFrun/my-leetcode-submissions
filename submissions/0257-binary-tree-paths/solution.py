# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def solve(node):
            if node.left == None and node.right == None:
                return [f'{node.val}']
            ret = []
            if node.left:
                ret.extend([f'{node.val}->{x}' for x in solve(node.left)])
            if node.right:
                ret.extend([f'{node.val}->{x}' for x in solve(node.right)])
            return ret
        return solve(root)
