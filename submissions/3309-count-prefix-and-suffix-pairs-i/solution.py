class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def solve(ps, word):
            if len(ps) > len(word):
                return False
            for i in range(len(ps)):
                if word[i] != ps[i] or word[- 1 - i] != ps[- 1 - i]:
                    return False
            return True
        
        ret = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if solve(words[i], words[j]):
                    ret += 1

        return ret

        
