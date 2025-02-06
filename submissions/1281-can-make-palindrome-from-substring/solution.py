class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        cts =[[0] * 26]
        for c in s:
            curr = [x for x in cts[-1]]
            curr[ord(c) - ord('a')] += 1
            cts.append(curr)
        
        def diffs(i, j):
            nonlocal cts
            left = cts[i]
            right = cts[j + 1]
            ret = [0] * 26
            for i in range(26):
                ret[i] = right[i] - left[i]
            return ret
        
        def solve(q):
            left = q[0]
            right = q[1]
            k = q[2]
            c = diffs(left, right)

            odds = 0
            for v in c:
                if v % 2 == 1:
                    odds += 1

            return (odds) // 2 <= k


        return [solve(q) for q in queries]
        
