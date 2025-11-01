class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ret = 0
        for s in sentences:
            ret = max(ret, len(s.split(' ')))
        return ret
