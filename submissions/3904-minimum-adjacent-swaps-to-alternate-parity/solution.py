class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ret = [0] * 4
        even_count, odd_count = 0, 0
        for i, num in enumerate(nums):
            if num % 2:
                ret[0] += abs((odd_count * 2) - i)
                ret[1] += abs((odd_count * 2 + 1) - i)
                odd_count += 1
            else:
                ret[2] += abs((even_count * 2) - i)
                ret[3] += abs((even_count * 2 + 1) - i)
                even_count += 1

        print(ret)

        if abs(even_count - odd_count) > 1:
            return -1
        
        if even_count == odd_count:
            return min(ret)
        
        if even_count > odd_count:
            return ret[2]

        return ret[0]


        
