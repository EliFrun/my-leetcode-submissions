class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        cnt = 0
        for coin in coins:
            if cnt >= coin - 1:
                cnt += coin
            else:
                break

        return cnt + 1

        
