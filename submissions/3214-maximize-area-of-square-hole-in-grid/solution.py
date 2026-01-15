class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        prev = -1
        seq = 0
        best_h = 0
        for i in range(len(hBars)):
            if hBars[i] == prev + 1:
                seq += 1
            else:
                best_h = max(best_h, seq)
                seq = 1
            prev = hBars[i]

        best_h = max(best_h, seq)
        
        vBars.sort()
        prev = -1
        seq = 0
        best_v = 0
        for i in range(len(vBars)):
            if vBars[i] == prev + 1:
                seq += 1
            else:
                best_v = max(best_v, seq)
                seq = 1
            prev = vBars[i]
        
        best_v = max(best_v, seq)

        return (min(best_h, best_v) + 1) ** 2
        
