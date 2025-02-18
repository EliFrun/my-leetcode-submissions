# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        curr = [root]
        ret = []
        while not all([x == None for x in curr]):
            nxt = []
            for node in curr:
                ret.append(str(node.val) if node else 'N')
                if node != None:
                    nxt.extend([node.left, node.right])

            curr = nxt
        return ','.join(ret)
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(data.pop(0))
        curr = [root]
        while data:
            nxt = []
            for node in curr:
                if node != None:
                    left = data.pop(0) if data else 'N'
                    right = data.pop(0) if data else 'N'
                    node.left = TreeNode(int(left)) if left != 'N' else None
                    node.right = TreeNode(int(right)) if right != 'N' else None
                    nxt.extend([node.left, node.right])

            curr = nxt

        return root    


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
