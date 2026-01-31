class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = '{'
        for c in letters:
            if c > target and c < l:
                l = c

        if l == '{':
            return letters[0]
        return l
        
