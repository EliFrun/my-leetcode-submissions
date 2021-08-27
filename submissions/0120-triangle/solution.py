class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = []
        
        for i in range(len(triangle)):
            memo.append([0] * (i + 1))
            
        memo[0] = triangle[0]
            
        layer = 1
        for t in triangle[1:]:
            l = len(t)
            for i in enumerate(t):
                index = i[0]
                value = i[1]
                if index == 0:
                    memo[layer][index] = value + memo[layer - 1][index]
                elif index == l - 1:
                    memo[layer][index] = value + memo[layer - 1][index - 1]
                else:
                    memo[layer][index] = value + min(memo[layer - 1][index - 1], memo[layer - 1][index])
            
            layer += 1
            
        return min(memo[-1])
            
