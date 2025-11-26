class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        left_count = 0
        left_sum = 0
        right_sum = sum(nums)
        right_count = len(nums)

        ret = [0] * len(queries)

        idx = 0
        curr = 0
        for i, query in sorted(enumerate(queries), key=lambda x: (x[1], x[0])):
            while idx < len(nums) and nums[idx] <= query:
                left_sum += (nums[idx] - curr) * left_count
                right_sum -= (nums[idx] - curr) * right_count
                left_count += 1
                right_count -= 1
                curr = nums[idx]
                idx += 1
            if curr != query:
                left_sum += (query - curr) * left_count
                right_sum -= (query - curr) * right_count
                curr = query
            ret[i] = left_sum + right_sum
        return ret
            
            
        
