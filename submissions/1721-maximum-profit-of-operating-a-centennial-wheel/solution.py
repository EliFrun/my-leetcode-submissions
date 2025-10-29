class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if sum(customers) * boardingCost < runningCost * len(customers) // 4:
            return -1
        m = 0
        ret = -1
        curr = 0
        waiting = 0
        i = 0
        gondolas = [0,0,0,0]
        while i < len(customers) or waiting != 0:
            if i < len(customers):
                waiting += customers[i]
            to_board = min(4, waiting)
            curr += boardingCost * to_board
            waiting -= to_board
            gondolas[i % 4] = to_board

            i += 1
            curr -= runningCost
            if curr > m:
                m = curr
                ret = i

        return ret
            
        
