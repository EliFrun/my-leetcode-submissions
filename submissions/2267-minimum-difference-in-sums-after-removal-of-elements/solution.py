class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        h1 = [-x for x in nums[:n]]
        h2 = nums[2*n:]
        rem = nums[n:2 * n]
        heapify(h1)
        heapify(h2)

        s1 = -sum(h1)
        l1 = [s1]
        for num in rem:
            if -num > h1[0]:
                s1 += heappop(h1)
                s1 += num
                heappush(h1, -num)
            l1.append(s1)

        s2 = sum(h2)
        l2 = [s2]
        for num in reversed(rem):
            if num > h2[0]:
                s2 -= heappop(h2)
                s2 += num
                heappush(h2, num)
            l2.append(s2)

        l2 = l2[::-1]
        ret = float('inf')
        for v1, v2 in zip(l1, l2):
            ret = min(ret, v1 - v2)
           
        return ret
