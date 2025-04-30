class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        left, right = defaultdict(list), defaultdict(list)
        for i, num in enumerate(nums):
            right[num].append(i)
        c = [0] * len(nums)
        l,r = 0, sum(nums)
        ret = 0
        for i,num in enumerate(nums[:len(nums) - 1]):
            left[num].append(i)
            right[num].pop(0)
            l += num
            r -= num
            if l == r:
                ret += 1
            if r - l + k in right:
                for i in right[r - l + k]:
                    c[i] += 1
            if l - r + k in left:
                for i in left[l - r + k]:
                    c[i] += 1

        return max(c + [ret])
