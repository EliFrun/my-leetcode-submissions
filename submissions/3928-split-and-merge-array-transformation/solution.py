class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        seen = set()
        curr = set([tuple(nums1)])
        nums2 = tuple(nums2)
        cnt = -1
        while curr:
            cnt += 1
            nxt = set()
            for lis in curr:
                if lis in seen:
                    continue
                seen.add(lis)
                if lis == nums2:
                    return cnt
                for i in range(len(nums1)):
                    for j in range(i + 1, len(nums1) + 1):
                        new_lis = lis[:i] + lis[j:]
                        for k in range(len(new_lis)):
                            tmp = tuple(new_lis[:k] + lis[i:j] + new_lis[k:])
                            nxt.add(tmp)

                curr = nxt - seen
        return -1
