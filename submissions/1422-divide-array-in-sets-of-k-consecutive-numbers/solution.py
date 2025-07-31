class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        s = SortedList(nums)

        while s:
            v = s[0]
            for i in range(v, v + k):
                if i in s:
                    s.remove(i)
                else:
                    return False

        return True
        
