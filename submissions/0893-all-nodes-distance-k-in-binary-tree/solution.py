# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d = {}
        # step 1: need to find "golden path"
        # all nodes on golden path with be labeled with distances from k
        def dfs(curr, distance_from_node):
            if not curr:
                return None
            if curr == target:
                distance_from_node = 0

            if distance_from_node is not None:
                d[curr.val] = distance_from_node
                dfs(curr.left, distance_from_node + 1)
                dfs(curr.right, distance_from_node + 1)
                return distance_from_node
            elif distance_from_node is None:
                l = dfs(curr.left, None)
                if l is not None:
                    l += 1
                    dfs(curr.right, l + 1)
                    d[curr.val] = l
                    return l
                r = dfs(curr.right, None)
                if r is not None:
                    r += 1
                    dfs(curr.left, r + 1)
                    d[curr.val] = r
                    return r

            

        
        
        dfs(root, None)
        return [key for key,v in d.items() if v == k]





