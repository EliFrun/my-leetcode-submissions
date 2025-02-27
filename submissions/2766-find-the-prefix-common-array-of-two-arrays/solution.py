class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        def common(a,b):
            ret = 0
            for i in range(len(A)):
                ret += min(a[i], b[i])
            return ret
        c_a = [0] * len(A)
        c_b = [0] * len(B)

        ret = []
        for a,b in zip(A, B):
            c_a[a - 1] += 1
            c_b[b - 1] += 1
            ret.append(common(c_a, c_b))

        return ret


        
