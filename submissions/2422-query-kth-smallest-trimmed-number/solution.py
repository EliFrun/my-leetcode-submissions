class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        l = defaultdict(list)
        ret = []
        for k, t in queries:
            if t not in l:
                for i, num in enumerate(nums):
                    l[t].append((int(num[-t:]), i))
                l[t].sort()
            ret.append(l[t][k - 1][1])
        
        return ret

        

        
        
