class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        dp = [[-1] * 2 ** len(cost[0]) for _ in range(2 ** len(cost))]
        def solve(left_enc, right_enc):
            if (v := dp[left_enc][right_enc]) != -1:
                return v
            i = 0
            while i < len(cost):
                if not (left_enc >> i) & 1:
                    ret = float('inf')
                    for j in range(len(cost[0])):
                        if (v := cost[i][j] + solve(left_enc | (1 << i), right_enc | (1 << j))) < ret:
                            ret = v
                    dp[left_enc][right_enc] = ret
                    return ret
                i += 1

            j = 0
            while j < len(cost[0]):
                if not (right_enc >> j) & 1:
                    ret = float('inf')
                    for i in range(len(cost)):
                        if (v := cost[i][j] + solve(left_enc, right_enc | (1 << j))) < ret:
                            ret = v
                    dp[left_enc][right_enc] = ret
                    return ret
                j += 1

            return 0
        return solve(0, 0)
            


        
