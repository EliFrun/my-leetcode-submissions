class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        for i in range(ceil(len(s)/k)):
            ret.append(s[k * i: (i + 1) * k])

        ret[-1] += fill * ((k - len(s) % k) % k)
        return ret
        
