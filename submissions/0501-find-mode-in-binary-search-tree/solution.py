# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(n):
            if not n:
                return []
            return inorder(n.left) +  [n.val] + inorder(n.right)
        
        a = defaultdict(int)
        for i in inorder(root):
            a[i] += 1
            
        ret = []
        m = 0
        for k,v in a.items():
            if v > m:
                ret = [k]
                m = v
            elif v == m:
                ret.append(k)
                
        return ret
