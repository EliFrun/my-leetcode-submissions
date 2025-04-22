# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, path):
            if not node:
                return False
            path.append(node)
            if node.val < key:
                return dfs(node.right, path)
            elif node.val > key:
                return dfs(node.left, path)
            return True

        p = []
        if not dfs(root, p):
            return root

        left, right = p[-1].left, p[-1].right
        
        if len(p) == 1:
            if not left and not right:
                return None
            if left:
                root = left
                while left.right:
                    left = left.right
                left.right = right
            elif right:
                root = right
                while right.left:
                    right = right.left
                right.left = left
            return root

        if p[-2].val > p[-1].val:
            p[-2].left = right
            if not right:
                p[-2].left = left
                return root
            while right.left:
                right = right.left
            right.left = left
        else:
            p[-2].right = left
            if not left:
                p[-2].right = right
                return root
            while left.right:
                left = left.right
            left.right = right

        return root

        
        
