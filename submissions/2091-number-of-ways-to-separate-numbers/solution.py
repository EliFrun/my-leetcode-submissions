class Solution:
    def numberOfCombinations(self, num: str) -> int:
        M = 1_000_000_007
        # str integer comparision function
        def gt(s1, s2):
            if len(s1) == len(s2):
                return s1 > s2
            return len(s1) > len(s2)
                
        if num[0] == '0':
            return 0

        dp = [[0] * (i + 1) for i in range(len(num))]
        dp[0][0] = 1
        prefix = [[0] * (i + 2) for i in range(len(num))]
        prefix[0][1] = prefix[0][0] + dp[0][0]
        # upper_bound
        for i in range(1, len(num)):
            # can always make a number where lower_bound is 0
            dp[i][0] = 1
            # lower_bound
            for j in range(i + 1):
                if num[j] == '0':
                    continue
                # current string is num[j:i + 1]
                # need to add all ways for all num[k:j] where k is between j - (length of num[j:i + 1]) and j
                # can add all when constraint that i + 1 - j > j - k
                # and if i + 1 - j == j - k, can only add when num[k:j] <= num[j:i + 1]
                # manually iterating is O(n ^ 3)
                # if we compute a prefix sum, it becomes O(n ^ 2)
                l = i - j + 1
                lower_bound = max(0, j - l)
                if gt(num[j - l:j], num[j:i + 1]):
                    lower_bound += 1
                   
                dp[i][j] = (dp[i][j] + prefix[j - 1][j] - prefix[j - 1][lower_bound] + M) % M
            
            # compute prefix sum for next upper_bound
            for k, v in enumerate(dp[i]):
                prefix[i][k + 1] = (prefix[i][k] + v) % M
                
        return sum(dp[-1]) % M
