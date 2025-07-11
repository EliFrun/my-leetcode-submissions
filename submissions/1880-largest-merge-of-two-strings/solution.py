class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        @cache
        def solve(i, j):
            if i >= len(word1):
                return word2[j:]
            if j >= len(word2):
                return word1[i:]
            if word1[i:] > word2[j:]:
                return word1[i] + solve(i + 1, j)
            return word2[j] + solve(i, j + 1)

        return solve(0, 0)
        
