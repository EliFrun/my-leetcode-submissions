class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        q = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()
        ret = []
        v = 0
        while v < k:
            _, i, j = heappop(q)
            if (i, j) in visited:
                continue
            visited.add((i,j))
            v += 1
            ret.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                heappush(q, (nums1[i + 1] + nums2[j], i + 1, j))

            if j + 1 < len(nums2):
                heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))

        return ret


        
