class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = []
        for word in words:
            for w in words:
                if word in w and word != w:
                    ret.append(word)
                    break

        return ret
        
