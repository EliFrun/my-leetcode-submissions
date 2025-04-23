class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a = sorted(zip(nums1, nums2), key=lambda x: x[1])
        q = [x[0] for x in a[len(a) - k:]]
        heapify(q)
        s = sum(q)
        ret = a[len(a) - k][1] * s
        for n1, n2 in reversed(a[:len(a) - k]):
            if n1 < q[0]:
                continue
            s -= heappop(q)
            s += n1
            ret = max(ret, s * n2)
            heappush(q, n1)

        return ret

        
