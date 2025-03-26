class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        l = defaultdict(list)
        for i, num in enumerate(nums):
            l[num].append(i)

        def best(q):
            num = nums[q]
            indexes = l[num]
            if len(indexes) <= 1:
                return -1
            idx = bisect_left(indexes, q)
            if idx == 0:
                return min(indexes[1] - indexes[0], indexes[0] + len(nums) - indexes[-1])
            elif idx == len(indexes) - 1:
                return min(indexes[idx] - indexes[idx - 1], len(nums) - indexes[idx] + indexes[0])
            else:
                return min(indexes[idx] - indexes[idx - 1], indexes[idx + 1] - indexes[idx])

        return [best(q) for q in queries]
            
