class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ret = [0] * len(code)
        for i in range(len(ret)):
            if code[i] == 0:
                continue
            elif k * code[i] > 0:
                for j in range(abs(k)):
                    ret[i] += code[(i + j + 1)%len(code)]
            else:
                for j in range(abs(k)):
                    ret[i] += code[(len(code) + i - j - 1)%len(code)]

        return ret
        
