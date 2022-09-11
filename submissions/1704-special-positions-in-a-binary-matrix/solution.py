class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ret = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if mat[i].count(1) == 1 and [x[j] for x in mat].count(1) == 1:
                        ret += 1
                        
        return ret
        
