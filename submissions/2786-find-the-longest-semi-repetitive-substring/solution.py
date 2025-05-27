class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        def solve(st):
            curr = '#'
            lis = []
            count = 0
            for c in st:
                if c == curr:
                    count += 1
                else:
                    lis.append(count)
                    count = 1
                    curr = c

            lis.append(count)
            return max(lis) <= 2 and Counter(lis).get(2, 0) <= 1


        left = 0
        ret = 0
        for i in range(len(s) + 1):
            while not solve(s[left:i]):
                left += 1

            ret = max(ret, i - left)
        
        return ret
                
