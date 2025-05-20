class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d = defaultdict(SortedList)
        for u, t in access_times:
            d[u].add(60 * int(t[:2]) + int(t[2:]))
        
        ret = []
        for u, times in d.items():
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] < 60:
                    ret.append(u)
                    break
        
        return ret

        
