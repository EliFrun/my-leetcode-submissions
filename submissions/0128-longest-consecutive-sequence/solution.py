class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        curr = nums[0]
        
        longest_seq = 1
        curr_seq = 1
        
        for i in nums:
            if i == curr + 1:
                curr_seq += 1
                longest_seq = max(curr_seq, longest_seq)
            elif i == curr:
                longest_seq = max(curr_seq, longest_seq)
            else:
                curr_seq = 1
            
            curr = i
            
        return longest_seq
