class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def anagram(w1, w2):
            c1 = Counter(w1)
            c2 = Counter(w2)
            for k in set(c1.keys()) | set(c2.keys()):
                if c1[k] != c2[k]:
                    return False
            return True
        
        remove = 0
        while remove >= 0:
            remove = -1
            for i in range(1, len(words)):
                if anagram(words[i], words[i - 1]):
                    remove = i
                    break
            if remove >= 0:
                words.pop(remove)
        return words
        
