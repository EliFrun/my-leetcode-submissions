class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stk = []
        if preorder[0] != '#':
            stk.append([preorder[0], 2])
        for c in preorder[1:]:
            if not stk:
                return False
            stk[-1][1] -= 1
            if stk[-1][1] == 0:
                stk.pop()
            if c != '#':
                stk.append([c, 2])

        return not stk
            
        
        
