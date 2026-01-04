class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        numbers = []
        for c in s:
            if c.isnumeric():
                numbers.append(c)
            else:
                letters.append(c)
        if abs(len(letters) - len(numbers)) > 1:
            return ""

        ret = ""
        while letters and numbers:
            ret += letters.pop()
            ret += numbers.pop()
        
        if letters:
            ret += letters.pop()
        if numbers:
            ret = numbers.pop() + ret
        return ret
