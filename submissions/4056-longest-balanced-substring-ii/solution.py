class Solution:
    def longestBalanced(self, s: str) -> int:
        ret = 1
        cnt = 0
        p = ''
        l = []
        
        a,b,c = 0,0,0
        da,db,dc = {0: -1}, {0: -1}, {0: -1}
        prev = {(0,0): -1}
        for i, ch in enumerate(s):
            if ch == p:
                cnt += 1
            else:
                ret = max(ret, cnt)
                cnt = 1
                p = ch
            if ch == 'a':
                a += 1
                da = {}
            elif ch == 'b':
                b += 1
                db = {}
            else:
                c += 1
                dc = {}

            if b - c not in da:
                da[b - c] = i
            if a - c not in db:
                db[a - c] = i
            if a - b not in dc:
                dc[a - b] = i

            if a - b in dc:
                ret = max(ret, i - dc[a - b])
            if a - c in db:
                ret = max(ret, i - db[a - c])
            if b - c in da:
                ret = max(ret, i - da[b - c])

            if (a - b, a - c) not in prev:
                prev[(a-b,a-c)] = i
            else:
                ret = max(ret, i - prev[(a-b,a-c)])

        ret = max(ret, cnt)
        return ret      
        
