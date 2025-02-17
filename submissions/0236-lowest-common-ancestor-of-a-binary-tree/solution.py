# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(node, val):
            if node == None:
                return []
            print(node.val, val)
            if node.val == val:
                return [node]
            left_path = solve(node.left, val)
            if len(left_path) > 0:
                return [node] + left_path
            right_path = solve(node.right, val)
            if len(right_path) > 0:
                return [node] + right_path
            return []

        p_path = solve(root, p.val)
        q_path = solve(root, q.val)


        ret = p_path[0]
        for pn, qn in zip(p_path, q_path):
            if pn.val != qn.val:
                break
            ret = pn
        
        return ret
            
        
