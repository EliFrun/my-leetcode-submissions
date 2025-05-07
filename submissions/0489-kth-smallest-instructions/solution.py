class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        j,i = destination
        @cache
        def solve(x,y):
            nonlocal k
            if x == i:
                return 'V' * (j - y)
            if y == j:
                return 'H' * (i - x)
            xp = i - x
            yp = j - y
            combos = comb(xp + yp - 1, xp - 1)
            if  combos >= k:
                return "H" + solve(x + 1, y)
            k  -= combos
            return "V" + solve(x, y + 1)

        return solve(0,0)
            


            
        
