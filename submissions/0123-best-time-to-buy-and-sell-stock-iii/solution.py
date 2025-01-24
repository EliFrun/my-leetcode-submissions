class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = [0] * len(prices)
        m = prices[0]
        for i in range(len(prices)):
            m = min(m, prices[i])
            lowest[i] = m
        
        highest = [0] * len(prices)
        mi = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            m = max(m, prices[i])
            highest[i] = m



        foo = [[y - x, z - y] for x,y,z in zip(lowest, prices, highest)]
        m = foo[-1][1]
        for i in range(len(foo) - 1, -1, -1):
            print(m)
            m = max(m, foo[i][1])
            foo[i][1] = m

        return max([sum(x) for x in foo])
        
        
