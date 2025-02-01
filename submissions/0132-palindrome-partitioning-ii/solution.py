class Solution:
    def minCut(self, s: str) -> int:
        @functools.cache
        def is_pal(i, j):
            if j <= i:
                return True
            if s[i] != s[j]:
                return False
            return is_pal(i + 1, j - 1)
        
        @functools.cache
        def palindrome_partitions(left):
            if left == len(s):
                return 0
            ret = len(s) - left
            for i in range(left, len(s)):
                if is_pal(left, i):
                    ret = min(ret, 1 + palindrome_partitions(i + 1))
            return ret
        
        return palindrome_partitions(0) - 1
