class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lis = self.generate_permutation(n)
        foo = [int(x) for x in lis]
        
        foo.sort()
        
        return str(foo[k - 1])
        
        
        
        
    def generate_permutation(self, n):
        if n == 1:
            return ["1"]
        
        ret = []
        for i in self.generate_permutation(n - 1):
            for j in range(n):
                ret.append(i[0:j] + str(n) + i[j:])
                
        return ret
