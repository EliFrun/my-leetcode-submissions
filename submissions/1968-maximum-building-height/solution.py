class Solution:
    def maxBuilding(self, n: int, r: List[List[int]]) -> int:
        r.append([1,0])
        r.sort()
        if r[-1][0] != n:
            r.append([n, float('inf')])

        ret = 0
        for i in range(len(r) - 1):
            currid, currh = r[i]
            nxtid, nxth = r[i + 1]
            distance = nxtid - currid
            if nxth > currh + distance:
                r[i + 1][1] = currh + distance

        for i in range(len(r) - 1, 0, -1):
            currid, currh = r[i]
            nxtid, nxth = r[i - 1]
            distance = currid - nxtid
            if nxth > currh + distance:
                r[i - 1][1] = currh + distance

        
        ret = 0
        for i in range(len(r) - 1):
            currid, currh = r[i]
            nxtid, nxth = r[i + 1]
            distance = nxtid - currid
            ret = max(ret, max(currh, nxth) + (distance - abs(nxth - currh)) // 2)
        return ret



