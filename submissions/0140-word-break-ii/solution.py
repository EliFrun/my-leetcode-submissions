class Solution:
    def wordBreak(self, st: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        @functools.cache
        def solve(s):
            if s == '':
                return [[]]
            ret = []
            for i in range(len(s) + 1):
                if s[:i] in wordDict:
                    ret.extend([[s[:i]] + x for x in solve(s[i:])])

            return ret
        return [' '.join(x) for x in solve(st)]
