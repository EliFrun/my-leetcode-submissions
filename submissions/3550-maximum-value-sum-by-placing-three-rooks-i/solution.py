class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        board = [sorted(list(enumerate(board[i])), key=lambda x: x[1])[-3:][::-1] for i in range(len(board))]

        s = defaultdict(SortedList)
        for row in board:
            for i,v in row:
                s[i].add(v)

        for row in board:
            for i in range(len(row) - 1, -1, -1):
                j, v = row[i]
                if len(s[j]) >= 3 and s[j][-3] > v:
                    row.pop(i)
        

        board = [x for x in board if x]

        row_bests = []
        for i, row in enumerate(board):
            row_bests.extend(sorted([(v,(i,j)) for j,v in row])[-3:])

        @cache
        def solve(i_taken, j_taken):
            if len(i_taken) == 3:
                return 0
            h = [(-v, (i,j)) for v, (i,j) in row_bests if i not in i_taken and j not in j_taken]
            heapify(h)
            ret = float("-inf")
            for _ in range(min(4, len(h))):
                v, (i,j) = heappop(h)
                ret = max(ret, -v + solve(
                        tuple(sorted(list(i_taken) + [i])),
                        tuple(sorted(list(j_taken) + [j]))
                    )
                )

            return ret

        return solve((), ())
                
            
            


        
