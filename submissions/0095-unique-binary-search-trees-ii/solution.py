# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ret = []
        for i in list(permutations([x for x in range(1, n + 1)])):
            root = TreeNode(i[0])
            for v in i[1:]:
                self.insertNode(root, TreeNode(v))
            ret.append(root)
            
        foo = {}
        
        for r in ret:
            foo[self.dfsTraversal(r)] = r
            
            
        return list(foo.values())
                
        
    def dfsTraversal(self, root):
        visiting = [root]
        to_visit = []
        ret = []
        while visiting:
            for n in visiting:
                if n:
                    to_visit.append(n.left)
                    to_visit.append(n.right)
                ret.append(n.val if n else n)
            visiting = to_visit
            to_visit = []
            
        return tuple(ret)
            
        
        
    def insertNode(self, root, new):
        if new.val > root.val:
            if not root.right:
                root.right = new
            else:
                self.insertNode(root.right, new)
                
        elif new.val < root.val:
            if not root.left:
                root.left = new
            else:
                self.insertNode(root.left, new)
        
