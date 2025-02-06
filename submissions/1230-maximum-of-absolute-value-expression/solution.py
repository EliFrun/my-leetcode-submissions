class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        mi, ma = [1_000_000] * 4, [-1_000_000] * 4
        for i in range(len(arr1)):
            vals = [
                arr1[i] + arr2[i] + i,
                arr1[i] - arr2[i] + i,
                - arr1[i] + arr2[i] + i,
                - arr1[i] - arr2[i] + i
            ]
            for j in range(4):
                if vals[j] < mi[j]:
                    mi[j] = vals[j]
                if vals[j] > ma[j]:
                    ma[j] = vals[j]


        ret = 0
        for i in range(4):
            ret = max(ret, ma[i] - mi[i])

        return ret
        
