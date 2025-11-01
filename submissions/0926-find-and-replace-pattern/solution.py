class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ret = []
        def mp(word):
            curr = 'a'
            m = {}
            res = ''
            for c in word:
                if c not in m:
                    m[c] = curr
                    curr = chr(ord(curr) + 1)
                res += m[c]
            return res

        pattern = mp(pattern)

        for word in words:
            if mp(word) == pattern:
                ret.append(word)
        return ret
            
        
