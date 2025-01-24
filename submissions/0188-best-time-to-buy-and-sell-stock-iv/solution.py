class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def next_bottom(i):
            if i >= len(prices) - 1:
                return len(prices)
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1

            return i

        def next_top(i):
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            
            return i
         
        rallies = []
        i = next_bottom(0)
        while i < len(prices):
            bottom = prices[i]
            i = next_top(i)
            rallies.append((bottom, prices[i]))
            i = next_bottom(i)

        rallies = [(x[0], x[1], x[1] - x[0]) for x in rallies if x[1] - x[0] > 0]


        def merge_loss(r):
            loss = 10 ** 10
            idx = 0
            for i in range(len(r) - 1):
                r1 = r[i]
                r2 = r[i + 1]
                gains = r1[2] + r2[2]
                c_gains = r2[1] - r1[0]
                if gains - c_gains < loss:
                    loss = gains - c_gains
                    idx = i


            return (loss, idx, idx + 1)


        def drop_loss(r):
            loss = 10 ** 10
            idx = 0
            for i in range(len(r)):
                if r[i][2] < loss:
                    idx = i
                    loss = r[i][2]

            return (loss, idx)

        
        def solve(r):
            if len(r) == 0:
                return 0
            if len(r) <= k:
                return sum([x[2] for x in r])

            ml, idx1, idx2 = merge_loss(r)
            dl, idx = drop_loss(r)

            if ml < dl:
                return solve(
                    r[:idx1] +
                    [(r[idx1][0], r[idx2][1], r[idx2][1] - r[idx1][0])] +
                    r[min(len(r), idx2 + 1):]
                )
            return solve(r[:idx] + r[min(len(r), idx + 1):])
        return solve(rallies)
            
        

        
            

        
