class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        bits = defaultdict(int)
        for i in range(len(nums)):
            for j in range(len(nums)):
                num = nums[i] & nums[j]
                bits[num] += 1


        ret = 0
        for num in nums:
            for key in bits.keys():
                if not key & num:
                    ret += bits[key]
        return ret
        
