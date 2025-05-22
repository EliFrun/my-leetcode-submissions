class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: (x[0], -x[1]))

        ret = 0
        k = 0
        h = []
        for i in range(len(nums)):
            while k < len(queries) and queries[k][0] <= i:
                heappush(h, -queries[k][1])
                k += 1

            if nums[i] <= 0:
                continue
            if not h:
                return -1
            diff = [0] * (-h[0] - i + 2)
            for _ in range(nums[i]):
                if not h:
                    return -1
                e = heappop(h)
                if -e < i:
                    return -1
                diff[0] += 1
                diff[-e - i + 1] -= 1

            c = 0
            for j in range(len(diff) - 1):
                c += diff[j]
                nums[i + j] -= c
            
        return len(h)

        
