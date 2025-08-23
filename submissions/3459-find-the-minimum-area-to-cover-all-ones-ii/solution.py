class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        if all(all([x == 1 for x in grid[i]]) for i in range(len(grid))):
            return len(grid[0]) * len(grid)
        @cache
        def solve(li, lj, hi, hj):
            mi, mmi, mj, mmj = float('inf'), 0, float('inf'), 0
            one_seen = False
            for i in range(li, hi + 1):
                for j in range(lj, hj + 1):
                    if grid[i][j]:
                        one_seen = True
                        mi = min(mi, i)
                        mmi = max(mmi, i)
                        mj = min(mj, j)
                        mmj = max(mmj, j)

            if not one_seen:
                return 0
            return (mmi - mi + 1) * (mmj - mj + 1)


        @cache
        def solve2(li, lj, hi, hj, left):
            ret = float('inf')
            for i in range(li, hi + 1):
                for j in range(lj, hj + 1):
                    curr = solve(li, lj, i, j)
                    
                    opt11 = solve(i + 1, lj, hi, hj)
                    opt12 = solve(li, j + 1, i, hj)

                    opt21 = solve(i + 1, lj, hi, j)
                    opt22 = solve(li, j + 1, hi, hj)

                    if i == 0 and j == 2:
                        print(left, curr, opt11, opt12, opt21, opt22)

                    if left == 1:
                        if opt11 == 0 or opt12 == 0:
                            ret = min(ret, curr + opt11 + opt12)
                        if opt21 == 0 or opt22 == 0:
                            ret = min(ret, curr + opt21 + opt22)
                    
                    
                    if left == 2:
                        ret = min(ret, curr + opt11 + opt12)
                        if opt11 == 0:
                            ret = min(ret, curr + solve2(li, j + 1, i, hj, 1))
                        if opt12 == 0:
                            ret = min(ret, curr + solve2(i + 1, lj, hi, hj, 1))

                        ret = min(ret, curr + opt21 + opt22)
                        if opt21 == 0:
                            ret = min(ret, curr + solve2(li, j + 1, hi, hj, 1))
                        if opt22 == 0:
                            ret = min(ret, curr + solve2(i + 1, lj, hi, j, 1))


            return ret

        return max(3, solve2(0, 0, len(grid) - 1, len(grid[0]) - 1, 2))
                    

                    
            
        
        
                    



        
