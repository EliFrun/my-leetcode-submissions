class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        nums = list(enumerate(nums))
        nums.sort(key=lambda x: (sum([int(y) for y in str(x[1])]), x[1]))
        visited = [False] * len(nums)
        cycles = 0
        for i in range(len(visited)):
            if visited[i]:
                continue
            visited[i] = True
            cycles += 1
            curr = nums[i][0]
            while curr != i:
                visited[curr] = True
                curr = nums[curr][0]

        return len(nums) - cycles
