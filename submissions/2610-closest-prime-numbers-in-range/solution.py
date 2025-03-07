class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        nums = [1 for _ in range(2, right + 1)]
        
        for j in range(2, len(nums), 2):
            nums[j] = 0
        for i in range(1, int(sqrt(right + 1)), 2):
            if nums[i] == 0:
                continue
            curr = i + 2
            for j in range(i + i + 2, len(nums), i + 2):
                nums[j] = 0

        prims = [i + 2 for i, v in enumerate(nums) if v == 1 and i + 2 >= left and i + 2 <= right]
        if len(prims) < 2:
            return [-1, -1]
        diff = prims[1] - prims[0]
        l, r = prims[0], prims[1]
        if diff <= 2:
            return [l, r]
        for i in range(1, len(prims) - 1):
            if prims[i + 1] - prims[i] < diff:
                diff = prims[i + 1] - prims[i]
                l = prims[i]
                r = prims[i + 1]
                if diff <= 2:
                    return [l, r]

        return [l, r]



        
