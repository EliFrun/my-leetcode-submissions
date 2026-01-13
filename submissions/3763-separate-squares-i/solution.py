class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        t = sum([l * l for _,_,l in squares])
        
        def solve(v):
            ret = 0
            for _, y, l in squares:
                if y > v:
                    ret += l * l
                elif y + l > v:
                    ret += (y + l - v) * l
            return t - ret < ret

        
        left, right = 0, max([y + l for _,y,l in squares])
        ret = -1
        while left <= right:
            middle = (left + right) / 2
            if solve(middle):
                ret = middle
                left = middle + 1e-6
            else:
                right = middle - 1e-6

        return ret

        
                
                
        
