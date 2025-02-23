# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def solve(pr, po):
            #print(pr, po)
            if not pr:
                return None
            ret = TreeNode(pr[0])
            pr = pr[1:]
            po = po[:-1]
            if len(pr) > 0 and len(po) > 0:
                left_pr = pr[0:pr.index(po[-1])]
                right_pr = pr[pr.index(po[-1]):len(pr)]
                left_po = [x for x in po if x in left_pr]
                right_po = [x for x in po if x in right_pr]
                ret.left = solve(left_pr, left_po)
                ret.right = solve(right_pr, right_po)
            return ret

        return solve(preorder, postorder)

        
