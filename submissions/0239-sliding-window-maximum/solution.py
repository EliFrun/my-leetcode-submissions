class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        current_window = [
            i for i,v in sorted(
                list(enumerate(nums[:k])), reverse=True, key=lambda x: (x[1], -x[0]))
        ]
        
        ret = [nums[current_window[0]]]
        for i in range(k, len(nums)):
            while current_window and current_window[0] <= i - k:
                current_window.pop(0)
            while current_window and nums[current_window[-1]] < nums[i]:
                current_window.pop()
            current_window.append(i)
            ret.append(nums[current_window[0]])
        return ret
            

            

        
