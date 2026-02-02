class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        l = SortedList(nums[len(nums) - dist:])
        l2 = SortedList()
        s = 0

        ret = float('inf')
        for i in range(len(nums) - 1, k - 2, -1):
            if nums[i] in l:
                l.remove(nums[i])
            else:
                l2.remove(nums[i])
                s -= nums[i]
            
            if i - dist > 0:
                l.add(nums[i - dist])
            while len(l2) < k - 2:
                v = l.pop(0)
                s += v
                l2.add(v)

            while l and l2 and l2[-1] > l[0]:
                v1 = l.pop(0)
                s += v1
                v2 = l2.pop(-1)
                s -= v2
                l.add(v2)
                l2.add(v1)


            ret = min(ret, nums[0] + s + nums[i])
        return ret



        
