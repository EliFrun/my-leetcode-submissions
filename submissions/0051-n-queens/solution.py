class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def new_list(): 
            return [['.' for _ in range(n)] for _ in range(n)]

        def make_copy(lis):
            ret = new_list()
            for i in range(n):
                for j in range(n):
                    ret[i][j] = lis[i][j]
            return ret

        def invalidate_squares(lis, i, j):
            # verticals
            for _i in range(n):
                if _i != i:
                    lis[_i][j] = 'x'
            
            # horizontals
            for _j in range(n):
                if _j != j:
                    lis[i][_j] = 'x'

            # diagonals 
            for _i in range(n):
                if _i == i:
                    continue
                diff = abs(_i - i)
                if j - diff >= 0:
                    lis[_i][j - diff] = 'x'
                if j + diff < n:
                    lis[_i][j + diff] = 'x'

        @functools.cache
        def has_valid_squares(serial_lis):
            lis = deserialize(serial_lis)
            for i in range(n):
                for j in range(n):
                    if lis[i][j] == '.':
                        return True
            return False

        def serialize(lis):
            return ''.join([''.join(row) for row in lis])

        def deserialize(lis_str):
            return [list(lis_str[n * i: n * (i + 1)]) for i in range(n)]

        @functools.cache
        def solve(serial_lis, left):
            lis = deserialize(serial_lis)
            if left == 0:
                return [lis]
            
            if not has_valid_squares(serial_lis):
                return []

            ret = []
            j = left - 1
            for i in range(n):
                if lis[i][j] == '.':
                    copy = make_copy(lis)
                    copy[i][j] = 'Q'
                    invalidate_squares(copy, i, j)
                    ret += solve(serialize(copy), left - 1)

            return ret

        def deduplicate_solutions(sols):
            uniq = list(set([serialize(sol).replace('x', '.') for sol in sols]))
            return [[u[n * i: n * (i + 1)] for i in range(n)] for u in uniq]


        
        return deduplicate_solutions(solve(serialize(new_list()), n))
            


        
