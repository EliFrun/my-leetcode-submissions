# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        layers = [[root]]
        while any(x != None for x in layers[-1]):
            nxt = []
            for node in layers[-1]:
                if not node:
                    nxt.extend([None, None])
                    continue
                nxt.append(node.left)
                nxt.append(node.right)
            layers.append(nxt)

        layers = layers[:len(layers) - 1]
        ret = [["" for _ in range(2**(len(layers)) - 1)] for __ in range(len(layers))]
        for i, layer in enumerate(layers):
            for j, x in enumerate(layer):
                st = len(ret[0]) // (2 ** (i + 1))
                ret[i][st + j * 2 ** (len(layers) - i)] = str(x.val) if x else ""
        return ret


        
