class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def solve(target):
            rem = k
            s = sum(stations[:r])
            l = []
            j = 0
            for i in range(len(stations)):
                if i + r < len(stations):
                    s += stations[i + r]
                while j < len(l) and l[j][0] < i - r:
                    s -= l[j][1]
                    j += 1
                if i - r - 1 >= 0:
                    s -= stations[i - r - 1]
                
                if s < target:
                    rem -= target - s
                    l.append((i + r, target - s))
                    s = target
                if rem < 0:
                    return False
                
            return True

        
        
        
        left, right = 0, sum(stations) + k
        ret = 0
        while left <= right:
            middle = (left + right) // 2
            if solve(middle):
                ret = middle
                left = middle + 1
            else:
                right = middle - 1
        
        return ret
