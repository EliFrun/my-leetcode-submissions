class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ret = [False] * len(s + " ")
        
        wordDict = set(wordDict)
        ret[0] = True
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if ret[i] and s[i: j + 1] in wordDict:
                    ret[j + 1] = True
                    
        return ret[-1]
