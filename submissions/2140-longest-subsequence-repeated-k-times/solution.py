class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        @cache
        def solve(i, word, count):
            if count == 0:
                return True
            if i >= len(s):
                return count == 0
            if len(s) - i < len(word) * count:
                return False

            idx = 0
            for j in range(i, len(s)):
                if s[j] == word[idx]:
                    idx += 1
                if idx >= len(word):
                    return solve(j + 1, word, count - 1)
            return False

        c = Counter(s)
        for key in list(c.keys()):
            if c[key] < k:
                c.pop(key)
        if not c:
            return ""
        s = "".join([x for x in s if x in c])
        c = Counter(s)
        

        letters = ''
        for key, value in c.items():
            letters += key * (value//k)
        
        max_length = len(s) // k
        l = list(reversed(sorted(set([''.join(x) for x in permutations(letters)]))))
        while len(l) > 0:
            for p in l:
                if solve(0, p, k):
                    return p
            l = list(reversed(sorted([x[1:] for x in l])))

        return ''
            
        

