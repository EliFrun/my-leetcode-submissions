class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        curr = []
        running = set()
        t = 0
        l = [0] * n
        for log in logs:
            p, action, ts = log.split(':')
            p = int(p)
            ts = int(ts)
            if action == 'start':
                if curr:
                    l[curr[-1]] += ts - t
                curr.append(p)
            elif action == 'end':
                ts += 1
                l[p] += ts - t
                curr.pop()
            t = ts
        return l


        
