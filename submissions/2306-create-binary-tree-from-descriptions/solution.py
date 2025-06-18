# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = defaultdict(lambda: [None, None])
        has_parent = set()

        for p, c, l in descriptions:
            d[p][1 - l] = c
            has_parent.add(c)


        root = set(d.keys()) - has_parent
        def build(node):
            if node == None:
                return node
            return TreeNode(node, build(d[node][0]), build(d[node][1]))

        return build(list(root)[0])
        
