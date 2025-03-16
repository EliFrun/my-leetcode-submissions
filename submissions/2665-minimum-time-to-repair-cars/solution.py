class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        def solve(m):
            fixed = 0
            for i in range(len(ranks)):
                fixed += int(sqrt(m/ranks[i]))
                if fixed >= cars:
                    return True
            return False
            

        left, right = 0, ranks[-1] * cars * cars
        while right - left > 1:
            middle = (left + right) // 2
            if solve(middle):
                right = middle
            else:
                left = middle

        if solve(left):
            return left
        return right
