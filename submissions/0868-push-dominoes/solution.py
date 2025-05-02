class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = dominoes
        ret = []
        prev = "L"
        curr = 0
        for c in s:
            if c == ".":
                curr += 1
            else:
                if curr > 0:
                    if prev == "L" and c == "R":
                        ret += ["."] * curr + [c]
                    elif prev == "L" and c == "L":
                        ret += ["L"] * (curr + 1)
                    elif prev == "R" and c == "R":
                        ret += ["R"] * (curr + 1)
                    else:
                        ret += ["R"] * (curr // 2)
                        if curr & 1:
                            ret += ['.']
                        ret += ["L"] * (curr // 2 + 1)
                else:
                    ret +=[c]
                prev = c
                curr = 0
        if curr > 0:
            if prev == "L":
                ret += ['.'] * curr
            else:
                ret += ["R"] * curr
        return "".join(ret)
            
        
