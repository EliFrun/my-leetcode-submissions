class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ret = 0
        curr = [0] * len(mat[0])
        for l in mat:
            for j in range(len(l)):
                curr[j] = curr[j] + l[j] if l[j] else 0
                h = float('inf')
                for k in range(j, -1, -1):
                    if curr[k] == 0:
                        break
                    h = min(h, curr[k])
                    ret += h
        return ret
            

        
