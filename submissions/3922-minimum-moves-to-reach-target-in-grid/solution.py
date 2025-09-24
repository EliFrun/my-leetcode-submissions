class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if (sx, sy) == (tx, ty):
            return 0

        if (sx, sy) == (0,0):
            return -1
        
        cnt = 0
        while tx > sx or ty > sy:
            cnt += 1
            if tx < ty or (tx == ty and sx > sy):
                if tx * 2 <= ty:
                    if ty & 1:
                        break
                    ty //= 2
                else:
                    ty -= tx
            else:
                if ty * 2 <= tx:
                    if tx & 1:
                        break
                    tx //= 2
                else:
                    tx -= ty
        
        if (tx, ty) == (sx, sy):
            return cnt

        return -1

        
        
