class Solution:
    def kthFactor(self, n: int, index: int) -> int:
        factors = self.primeFactor(n)
        ret = [1]
        
        d = defaultdict(lambda: 0)
        
        for f in factors:
            d[f] += 1
        
        ret = [1]
        for k, v in d.items():
            foo = [k ** i for i in range(v + 1)]
            new_ret = []
            for r in ret:
                for f in foo:
                    new_ret.append(f * r)
            ret = new_ret
            
        ret.sort()
        return ret[index - 1] if index - 1 < len(ret) else  -1
        
    def primeFactor(self, n):
        if n == 1:
            return []
        
        if n % 2 == 0:
            return[2] + self.primeFactor(n // 2)
        
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return [i] + self.primeFactor(n // i)
            
        return [n]
