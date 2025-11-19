class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        curr = set([0,x,y])
    

        # for each given volume that can be obtained, we can do the following operations
        # 1. if volume < x, pour into x
        #    a. fill y. pour y into x until x is full => y - (x - a)
        # 2. if volume > x
        #    a. pour into x, y will have a - x left
        # 3. if volume < y pour into y
        #    a. fill x. pour x into y until y is full => x - (y - a)
        # 4. if volume > y
        #    a. pour into y, x will have a - y left
        # in summary, for each value, we can create (y + a - x), (x + a - y), (a - y), (a - x)

        seen = set()
        while curr:
            nxt = set()
            for v in curr:
                seen.add(v)
                for possibility in [y + v - x, v - x, x + v - y, v - y]:
                    if 0 <= possibility <= x + y:
                        nxt.add(possibility)

            curr = nxt - seen
        return target in seen or target - x in seen or target - y in seen

        
