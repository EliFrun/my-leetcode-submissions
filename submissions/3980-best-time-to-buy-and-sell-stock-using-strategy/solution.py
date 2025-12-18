class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        ret = sum([x * y for x,y in zip(prices, strategy)])
        
        curr_balance = 0
        k //= 2
        for i in range(k, 2 * k):
            curr_balance += prices[i]
        for i in range(2 * k, len(prices)):
            curr_balance += strategy[i] * prices[i]
        ret = max(ret, curr_balance)
        for i in range(len(prices) - 2 * k):
            curr_balance += strategy[i] * prices[i]
            curr_balance -= prices[k + i]
            curr_balance += prices[2 * k + i]
            curr_balance -= prices[2 * k + i] * strategy[2 * k + i]
            ret = max(ret, curr_balance)
        return ret
        
