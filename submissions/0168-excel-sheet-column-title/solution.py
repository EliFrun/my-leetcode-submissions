class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        l = int(log(columnNumber, 26))
              
        ret = []
        for i in range(l, -1, -1):
            ret.append(columnNumber // (26 ** i))
            columnNumber %= 26 ** i
            
        
        for i in range(len(ret) - 1, 0, -1):
            if ret[i] == 0:
                ret[i] += 26
                ret[i - 1] -= 1
                                
        i = 0
        while ret[i] == 0:
            i += 1
            
        ret = ret[i:]
        
        return "".join([chr(ord("A") + x - 1) for x in ret])
