class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            j = 0
            for i, c in enumerate(s):
                if c == word[j]:
                    j += 1
                if len(s) - i < len(word) - j:
                    break

                if j >= len(word):
                    return word
        return ''



        
