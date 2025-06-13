class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        logs = [[0,0]] + logs
        m = 0
        ret = -1
        for i in range(1, len(logs)):
            if logs[i][1] - logs[i - 1][1] > m:
                m = logs[i][1] - logs[i - 1][1]
                ret = logs[i][0]
            elif logs[i][1] - logs[i - 1][1] == m:
                ret = min(logs[i][0], ret)

        return ret
        
        

        
