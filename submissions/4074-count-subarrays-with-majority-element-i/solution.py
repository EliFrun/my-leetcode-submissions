class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        ret = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, -1, -1):
                if nums[j] == target:
                    cnt += 1
                if cnt > (i - j + 1)//2:
                    ret += 1
        return ret
                
        
