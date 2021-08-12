class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = '0'
        
        ret = ""
        
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a    
        
        for i in range(len(a) - 1, -1, -1):
            if a[i] == b[i]:
                ret = "0" + ret if carry == "0" else "1" + ret
                carry = "1" if a[i] == "1" else "0"
            else:
                ret = "1" + ret if carry == "0" else "0" + ret
                carry = "1" if carry == "1" else "0"
                
        if carry == "1":
            ret = "1" + ret
            
        return ret
                

