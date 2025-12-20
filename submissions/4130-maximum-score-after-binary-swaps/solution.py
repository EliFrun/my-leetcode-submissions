class Solution:
    def maximumScore(self, nums: List[int], st: str) -> int:
        s = SortedList()
        ret = 0
        for i, num in enumerate(nums):
            if st[i] == '1':
                if s and num <= s[-1]:
                    ret += s[-1]
                    s.pop(-1)
                    s.add(num)
                else:
                    ret += num
            else:
                s.add(num)
        return ret
