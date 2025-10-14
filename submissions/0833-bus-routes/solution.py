class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        routes = [set(x) for x in routes]
        curr = set([source])

        ret = -1
        prev_len = -1
        while prev_len != len(routes):
            prev_len = len(routes)
            nxt = set()
            
            ret += 1
            if target in curr:
                return ret
            
            to_pop = []
            for i in range(len(routes)):
                if routes[i] & curr:
                    nxt |= routes[i]
                    to_pop.append(i)
            curr |= nxt
            for i in reversed(to_pop):
                routes.pop(i)
            
        return -1
        
