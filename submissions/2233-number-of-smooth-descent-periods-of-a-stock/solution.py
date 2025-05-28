class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        curr = prices[0]
        count = 1
        lis = []
        for p in prices[1:]:
            if p == curr - 1:
                count += 1
            else:
                lis.append(count)
                count = 1
            curr = p

        lis.append(count)
        return sum([x * (x + 1) // 2 for x in lis])
