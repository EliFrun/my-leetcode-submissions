class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hd(w1, w2):
            ret = 0
            if len(w1) != len(w2):
                return False
            for l1, l2 in zip(w1,w2):
                if l1 != l2:
                    ret += 1
                if ret > 1:
                    return False
            return True

        
        @cache
        def solve(i):
            if i >= len(words):
                return []
            ret = [words[i]]
            new_ret = []
            for j in range(i + 1, len(words)):
                if hd(words[i], words[j]) and groups[i] != groups[j]:
                    res = solve(j)
                    if len(res) > len(new_ret):
                        new_ret = solve(j)
            return ret + new_ret

        ret = []
        for i in range(len(words)):
            res = solve(i)
            if len(res) > len(ret):
                ret = res

        return ret
        
