class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = SortedList(nums[:k])
        
        ret = [s[-1]]
        for i in range(k, len(nums)):
            s.add(nums[i])
            s.remove(nums[i - k])
            ret.append(s[-1])
           
        return ret
            

            

        
