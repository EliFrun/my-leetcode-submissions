class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        j, k = 0, 0
        nums.sort()
        closest = nums[0] + nums[1] + nums[-1]
        for i in range(0, len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while(j < k):
                if closest == target: 
                    break
                    
                value = nums[i] + nums[j] + nums[k]
                if value > target:
                    k-=1
                        
                if value < target:
                    j += 1
                    
                if abs(value - target) < abs(target - closest):
                        closest = value
                        
                        
        return closest
