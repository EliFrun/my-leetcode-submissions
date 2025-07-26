class Solution:
    def maxSubarrays(self, n: int, o_c: List[List[int]]) -> int:
        o_c = [sorted(l) for l in o_c]
        c = [(y, x) for x,y in o_c]
        heapify(c)
        d = defaultdict(int)
        s = [(0,0),(0,0)]

        for i in range(1, n + 1):
            while c and c[0][0] <= i:
                r, l = heappop(c)
                heappush(s, (l,r))
                while len(s) > 2:
                    heappop(s)
            
            d[s[-1]] += s[-1][0] - s[-2][0]


        best = sorted((v, k) for k,v in d.items())[-1][1]
        
        # combo counting
        c = [(y,x) for x,y in o_c if (x,y) != best]
        heapify(c)
        ret = 0
        boundary = (0,0)
        for i in range(1, n + 1):
            while c and c[0][0] <= i:
                r, l = heappop(c)
                if l >= boundary[0]:
                    boundary = (l,r)
        
            ret += i - boundary[0]

        return ret
            




            



        
