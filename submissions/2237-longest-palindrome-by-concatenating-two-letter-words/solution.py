class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        print(c)
        ret = 0
        middle = 0
        for k in c.keys():
            if k == k[::-1]:
                if c[k] & 1:
                    middle = 2
                ret += (c[k] // 2) * 4
            else:
                rev = k[::-1]
                if rev in c:
                    ret += 2 * min(c[k], c[rev])

        return ret + middle
            

        
