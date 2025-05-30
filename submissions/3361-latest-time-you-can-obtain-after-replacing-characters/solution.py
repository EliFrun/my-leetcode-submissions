class Solution:
    def findLatestTime(self, s: str) -> str:
        ret = list(s)
        for i in range(5):
            if s[i]== "?":
                if i == 0:
                    ret[i] = "1" if s[i + 1] in "?01" else "0"
                if i == 1:
                    if ret[i - 1] == "1":
                        ret[i] = "1"
                    else:
                        ret[i] = "9"
                if i == 3:
                    ret[i] = "5"
                if i == 4:
                    ret[i] = "9"

        return "".join(ret)        
