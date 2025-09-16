class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def eq(m1, m2):
            return all(
                all(
                    m1[i][j] == m2[i][j] for j in range(len(m1))
                ) for i in range(len(m1))
            )

        def rotate(m1):
            ret = [[0] * len(mat) for _ in range(len(mat))]
            for i in range(len(mat)):
                for j in range(len(mat)):
                    ret[i][j] = m1[j][len(mat) - i - 1]
            return ret

        for _ in range(4):
            if eq(mat, target):
                return True
            mat = rotate(mat)


        return False
        
