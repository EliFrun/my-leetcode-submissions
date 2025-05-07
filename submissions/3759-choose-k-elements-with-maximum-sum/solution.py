class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        nums = SortedList([(x,i) for i,x in enumerate(nums1)])
        h = []
        ret = []
        prev = -1
        s = 0
        for x,i in nums:
            if x == prev:
                ret.append((ret[-1][0], i))
            else:
                prev = x
                ret.append((s, i))
            if len(h) == k:
                v = h[0]
                if v < nums2[i]:
                    s -= v
                    s += nums2[i]
                    heappop(h)
                    heappush(h, nums2[i])
            else:
                s += nums2[i]
                heappush(h, nums2[i])

        return [x[0] for x in sorted(ret, key=lambda x:x[1])]
            
