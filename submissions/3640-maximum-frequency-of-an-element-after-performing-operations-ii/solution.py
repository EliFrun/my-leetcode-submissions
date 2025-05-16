class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        s = SortedList(nums)
        cands = set()
        for i in s:
            cands.update([i - k, i, i + k])
        
        s.add(-10 ** 10)
        s.add(10 ** 10)

        ret = 0
        i = 0
        for num in cands:
            #print(num)
            left = s.bisect_left(num) - s.bisect_left(num - k)
            middle = s.bisect_right(num) - s.bisect_left(num)
            right = s.bisect_right(num + k) - s.bisect_right(num)
            #print(left, middle, right)
            cand = left + right
            cand = min(cand, numOperations)
            ret = max(ret, cand + middle)
            if i == len(s) - 1:
                break
            if num + k < s[i + 1]:
                num += k
            else:
                i += 1
                num = s[i]

        return ret
        
