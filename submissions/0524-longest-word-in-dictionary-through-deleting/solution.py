class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            length = 0
            i = 0
            while length < len(word) and i < len(s) and len(word) - length <= len(s) - i:
                if word[length] == s[i]:
                    length += 1
                i += 1
            if length == len(word):
                return word
        return ''
