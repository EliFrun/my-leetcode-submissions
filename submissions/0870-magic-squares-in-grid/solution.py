class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(arr):
            if len(list(set(arr[0] + arr[1] + arr[2]))) != 9:
                return False
            
            if not all([1 <= x and x <= 9 for x in arr[0] + arr[1] + arr[2]]):
                return False
             
            return len(
                    set(
                        [
                            sum(arr[0]),
                            sum(arr[1]),
                            sum(arr[2]),
                            sum([x[0] for x in arr]),
                            sum([x[1] for x in arr]),
                            sum([x[2] for x in arr]),
                            sum([arr[0][0], arr[1][1], arr[2][2]]),
                            sum([arr[2][0], arr[1][1], arr[0][2]])
                        ]
                    )
                ) == 1
        
        ret = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if (isMagic([x[j: j+3] for x in grid[i:i+3]])):
                    ret += 1
                    
        return ret
        
