class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        curr = 1
        ret = []
        for t in target:
            if curr > n:
                break
            while curr < n and t > curr:
                ret.append('Push')
                ret.append('Pop')
                curr += 1
            ret.append('Push')
            curr += 1
        return ret
        
