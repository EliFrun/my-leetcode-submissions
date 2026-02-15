class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ret = ''
        a,b = list(a), list(b)
        while a or b:
            aa = 0
            if a:
                aa = int(a.pop())
            bb = 0
            if b:
                bb = int(b.pop())
            
            ret += str((aa + bb + carry) % 2)
            carry = (aa + bb + carry) // 2

        if carry:
            ret += '1'
        return ret[::-1]
        
