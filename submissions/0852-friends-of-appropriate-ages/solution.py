class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        d = defaultdict(lambda: 0)
        
        for age in ages:
            d[age] += 1
            
        ret = 0
        
        for key, value in d.items():
            for i in range(ceil(key / 2 + 7.5), key):
                if i in d:
                    ret += value * d[i]
            ret += value * (value - 1) if key / 2 + 7 < key else 0
       
        return ret
