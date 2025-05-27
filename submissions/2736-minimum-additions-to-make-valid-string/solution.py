class Solution:
    def addMinimum(self, word: str) -> int:
        ret = 0
        curr = ""
        for c in word:
            if c == "a":
                if curr != "":
                    ret += 3 - len(curr)
                curr = "a"
            if c == "b":
                if curr != "a":
                    ret += 1 if not curr else 2
                curr = "ab"
            if c == "c":
                if curr != "ab":
                    ret += 2 - len(curr)
                curr = ""
        if curr:
            ret += 3 - len(curr)
        return ret

        
