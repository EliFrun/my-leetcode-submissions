class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        curr = 1 - groups[0]
        ret = []
        for l,i in zip(words, groups):
            if i == curr:
                continue
            curr = i
            ret.append(l)

        return ret

        
