class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ret = []
        curr = 1 - groups[0]
        for word, group in zip(words, groups):
            #print(curr, word, group)
            if group != curr:
                ret.append(word)
                curr = group

        return ret
