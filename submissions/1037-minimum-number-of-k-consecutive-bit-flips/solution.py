class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        s = SortedList()
        for i in range(len(nums)):
            current_state = (nums[i] + len(s) - s.bisect_left(i)) % 2
            if current_state == 0:
                if i + k - 1 >= len(nums):
                    return -1
                s.add(i + k - 1)

        return len(s)
            
            
        
