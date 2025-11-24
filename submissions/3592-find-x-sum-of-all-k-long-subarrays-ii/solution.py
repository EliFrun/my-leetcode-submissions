class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        counts = defaultdict(int)
        lis1 = SortedList()
        lis2 = SortedList()
        ret = []
        s = 0
        for i in range(len(nums)):
            n = nums[i]
            if (counts[n], n) in lis1:
                lis1.remove((counts[n], n))
            elif (counts[n], n) in lis2:
                s -= counts[n] * n
                lis2.remove((counts[n], n))
            counts[n] += 1
            lis1.add((counts[n], n))

            if i < k - 1:
                continue

            while lis1 and len(lis2) < x:
                c1,v1 = lis1.pop()
                s += c1 * v1
                lis2.add((c1,v1))

            while lis1 and lis1[-1] > lis2[0]:
                c1, v1 = lis1.pop(-1)
                c2, v2 = lis2.pop(0)
                s -= c2 * v2
                s += c1 * v1
                lis1.add((c2, v2))
                lis2.add((c1, v1))

            ret.append(s)
            m = nums[i - k + 1]
            if (counts[m], m) in lis1:
                lis1.remove((counts[m], m))
            elif (counts[m], m) in lis2:
                s -= counts[m] * m
                lis2.remove((counts[m], m))
            counts[m] -= 1
            lis1.add((counts[m], m))

            
        return ret
