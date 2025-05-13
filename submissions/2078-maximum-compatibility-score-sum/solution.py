class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def similarity(x,y):
            return sum(1- i ^ j for i,j in zip(x,y))
        mat = [[similarity(x,y) for y in students] for x in mentors]


        @cache
        def solve(left):
            i = len(students) - len(left)
            left = set(left)
            ret = 0
            for v in left:
                ret = max(ret, mat[i][v] + solve(tuple(sorted(list(left - set([v]))))))

            return ret

        return solve(tuple(range(len(students))))
