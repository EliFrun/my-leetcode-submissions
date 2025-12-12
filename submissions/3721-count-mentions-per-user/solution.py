class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events = [(m, int(t), ms) for m,t,ms in events]
        events.sort(key=lambda x: (x[1], (1 if x[0] == 'MESSAGE' else 0)))
        online = [True] * numberOfUsers
        ret = [0] * numberOfUsers
        t = 0
        q = []
        for m, ts, ms in events:
            t = ts
            while q and q[0][0] <= t:
                _, i = heappop(q)
                online[i] = True
            if m == "OFFLINE":
                i = int(ms.replace('id', ''))
                heappush(
                    q,
                    (ts + 60, i)
                )
                online[i] = False
            else:
                ids = ms.split(' ')
                mentions = defaultdict(int)
                for i in ids:
                    i = i.replace('id', '')
                    if i == 'ALL':
                        for j in range(numberOfUsers):
                            mentions[j] += 1
                        break
                    elif i == 'HERE':
                        for j in [i for i,x in enumerate(online) if x]:
                            mentions[j] += 1
                    else:
                        mentions[int(i)] += 1
                for k, v in mentions.items():
                    ret[k] += v 
        return ret
                
            
        
