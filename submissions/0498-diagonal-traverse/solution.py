class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        curr = [0, 0]
        direction = 1
        ret = [-1] * (len(mat) * len(mat[0]))
        i = 0
        while i < len(mat[0]) * len(mat):
            while 0 <= curr[0] < len(mat) and 0 <= curr[1] < len(mat[0]):
                ret[i] = mat[curr[0]][curr[1]]
                i += 1
                if direction == 1:
                    curr[0] -= 1
                    curr[1] += 1
                else:
                    curr[0] += 1
                    curr[1] -= 1
            
            if direction == 1:
                curr[0] += 1
                curr[1] -= 1
                if curr[0] != 0 or curr[1] == len(mat[0]) - 1:
                    curr[0] += 1
                else:
                    curr[1] += 1
            else:
                curr[0] -= 1
                curr[1] += 1
                if curr[1] != 0 or curr[0] == len(mat) - 1:
                    curr[1] += 1
                else:
                    curr[0] += 1
            direction = 1 - direction

        return ret
