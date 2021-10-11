class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a = word.find(ch)
        a = a if a > 0 else 0
        return word[a::-1] + word[a + 1:]
