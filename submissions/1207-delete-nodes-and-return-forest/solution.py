# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ret = []
        to_delete = set(to_delete)
        if root.val not in to_delete:
            ret.append(root)
        curr = [root]
        while curr:
            nxt = []
            for node in curr:
                if not node:
                    continue
                nxt.append(node.left)
                nxt.append(node.right)
                if node.left and node.left.val in to_delete:
                    node.left = None
                if node.right and node.right.val in to_delete:
                    node.right = None
                if node and node.val in to_delete:
                    if node.left:
                        ret.append(node.left)
                    if node.right:
                        ret.append(node.right)
            curr = nxt

        return ret
        
