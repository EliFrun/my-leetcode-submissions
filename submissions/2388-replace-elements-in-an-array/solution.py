class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i,v in enumerate(nums):
            d[v].append(i)

        for b,a in operations:
            d[a].extend(d[b])
            d.pop(b)

        for k,v in d.items():
            for i in v:
                nums[i] = k

        return nums
        
