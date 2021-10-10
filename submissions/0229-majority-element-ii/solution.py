class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1
            
        ret = []
        for i, v in count.items():
            if v > len(nums) // 3:
                ret.append(i)
                
        return ret
