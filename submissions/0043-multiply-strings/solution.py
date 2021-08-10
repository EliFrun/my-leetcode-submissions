class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        adds = []
        i = 0
        for s in reversed(num2):
            adds.append(self.singleM(num1, s) + "0" * i)
            i+=1
        
        ret = adds[0]
        for s in adds[1:]:
            ret = self.add(ret, s)
            
        return ret
    
        
    def singleM(self, num1: str, num2: str) -> str:
        ret = ""
        carry = 0
        for s in reversed(num1):
            foo = int(s) * int(num2) + carry
            ret = f'{foo%10}{ret}'
            carry = foo // 10
        
        if carry:
            ret = f'{carry}' + ret
        
        return ret
      
    
    def add(self, num1: str, num2: str) -> str:
        carry = 0
        ret = ""
        if len(num1) > len(num2):
            num2 = "0" * (len(num1) - len(num2)) + num2
        elif len(num1) < len(num2):
             num1 = "0" * (len(num2) - len(num1)) + num1
        
        for i in range(len(num1) - 1, -1, -1):
            foo = int(num1[i]) + int(num2[i]) + carry
            ret = f'{foo%10}{ret}'
            carry = foo // 10
            
        if carry:
            ret = "1" + ret
        
        
        return ret
