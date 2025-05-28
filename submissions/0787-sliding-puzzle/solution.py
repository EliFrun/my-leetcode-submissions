class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        curr = set([tuple(board[0] + board[1])])
        visited = set()
        layer = -1
        while curr:
            layer += 1
            nxt = set()
            for b in curr:
                if b in visited:
                    continue
                visited.add(b)
                if b == (1,2,3,4,5,0):
                    return layer
                b = list(b)
                idx = b.index(0)
                if idx in [0,1,2] and idx - 1 >= 0 or idx in [3,4,5] and idx - 1 >= 3:
                    b[idx - 1], b[idx] = b[idx], b[idx - 1]
                    nxt.add(tuple(b))
                    b[idx - 1], b[idx] = b[idx], b[idx - 1]
                if idx in [0,1,2] and idx + 1 < 3 or idx in [3,4,5] and idx + 1 < 6:
                    b[idx + 1], b[idx] = b[idx], b[idx + 1]
                    nxt.add(tuple(b))
                    b[idx + 1], b[idx] = b[idx], b[idx + 1]

                if idx in [0,1,2]:
                    b[idx + 3], b[idx] = b[idx], b[idx + 3]
                    nxt.add(tuple(b))
                    b[idx + 3], b[idx] = b[idx], b[idx + 3]
                else:
                    b[idx - 3], b[idx] = b[idx], b[idx - 3]
                    nxt.add(tuple(b))
                    b[idx - 3], b[idx] = b[idx], b[idx - 3]

            curr = nxt - visited

        return -1

                    
