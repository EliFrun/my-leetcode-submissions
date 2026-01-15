class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort()
        
        discrete_x = set()
        for l, r, h in buildings:
           discrete_x.update([l, r])

        ret = []
        curr = SortedList([0])
        q = []
        i = 0
        prev = 0
        for x in sorted(list(discrete_x)):
            while i < len(buildings) and buildings[i][0] <= x: 
                l, r, h = buildings[i]
                curr.add(h)
                heappush(q, (r, h))
                i += 1

            while q and q[0][0] <= x:
                _, h = heappop(q)
                curr.remove(h)

            if curr[-1] != prev:
                ret.append([x, curr[-1]])

            prev = curr[-1]

        return ret


        
            
