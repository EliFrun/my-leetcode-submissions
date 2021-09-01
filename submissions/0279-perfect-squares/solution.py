class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        checking = set([n])
        to_check = set()
        
        layer = 0
        while checking:
            layer += 1
            for i in checking:
                largest_square = int(sqrt(i))
                for j in range(largest_square, 0, -1):
                    foo = i - j * j
                    if foo == 0:
                        return layer
                    to_check.add(foo)
                    
            checking = to_check
            to_check = set()
            
            
                
