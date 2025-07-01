class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = defaultdict(list)
        def to_time(s):
            h, m = s.split(':')
            return int(h) * 60 + int(m)

        ret = set()
        for n, t in sorted(list(zip(keyName, keyTime)), key=lambda x: to_time(x[1])):
            if n in ret:
                continue
            t = to_time(t)
            if times[n] and t < times[n][-1]:
                times[n] = []
            times[n].append(t)
            if len(times[n]) < 3:
                continue
            if times[n][-1] - times[n][-3] <= 60:
                ret.add(n)

        return sorted(list(ret))
        
