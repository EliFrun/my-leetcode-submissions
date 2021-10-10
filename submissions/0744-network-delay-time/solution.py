class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        for node in times:
            d[node[0]].append(node)
            
        
        time = [1000000000] * n
        for _ in range(2):
            visited = set()
            time[k - 1] = 0
            curr = d[k]

            while curr:
                to_visit = []
                for f, t, dis in curr:
                    time[t - 1] = min(time[t - 1], time[f - 1] + dis)
                    to_visit += d[t] if t not in visited else []
                    visited.add(f)

                curr = to_visit
        m = max(time)
        return m if m != 1000000000 else -1
                
