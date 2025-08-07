class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        res = 0
        for i in range(len(fruits)):
            res += fruits[i][i]
            fruits[i][i] = 0
        
        for i in range(len(fruits) - 2, -1, -1):
            lower = i + 1
            upper = len(fruits) - 1
            for j in range(lower, upper + 1):
                    fruits[i][j] += max([fruits[i + 1][j + k] for k in [-1, 0, 1] if lower <= j + k <= upper])

        for i in range(len(fruits) - 2, -1, -1):
            lower = i + 1
            upper = len(fruits) - 1
            for j in range(lower, upper + 1):
                    fruits[j][i] += max([fruits[j + k][i + 1] for k in [-1, 0, 1] if lower <= j + k <= upper])

        return res + fruits[-1][0] + fruits[0][-1]
