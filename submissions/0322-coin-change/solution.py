class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = [x for x in sorted(coins) if x <= amount][::-1]

        
        # bfs implementation
        curr = set([amount])
        visited = set()
        count = 0
        while curr:
            if 0 in curr:
                return count

            nxt = set()
            for i in curr:
                visited.add(i)
                for n in coins:
                    if i - n not in curr and i - n >= 0:
                        nxt.add(i - n)

            curr = nxt
            count += 1
        return -1
        
