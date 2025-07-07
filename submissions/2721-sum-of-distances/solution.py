class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left_counts = defaultdict(int)
        left_sums = defaultdict(int)
        right_counts = Counter(nums)
        right_sums = defaultdict(int)
        for i,v in enumerate(nums):
            right_sums[v] += i

        ret = []
        for i, v in enumerate(nums):
            right_counts[v] -= 1
            right_sums[v] -= i
            ret.append(right_sums[v] - right_counts[v] * i + left_counts[v] * i - left_sums[v])
            left_counts[v] += 1
            left_sums[v] += i

        return ret
