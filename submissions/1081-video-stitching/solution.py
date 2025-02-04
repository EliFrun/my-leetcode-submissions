class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key= lambda x: (x[1], x[0]))
        dp = [10000] * (101)
        for i in range(len(clips) - 1, -1, -1):
            s, e = clips[i]
            for j in range(s, e):
                if e >= time:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[j], 1 + dp[e])


        return dp[0] if dp[0] != 10000 else -1
        
