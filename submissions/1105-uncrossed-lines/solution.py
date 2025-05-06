class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = defaultdict(list)
        for i, num in enumerate(nums2):
            m[num].append(i)

        @cache
        def solve(i, ll):
            if i >= len(nums1):
                return 0
            ret = 0
            for idx in m[nums1[i]]:
                if idx > ll:
                    ret = 1 + solve(i + 1, idx)
                    break

            return max(ret, solve(i + 1, ll))

        return solve(0, -1)


        
        
