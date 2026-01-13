class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        d = defaultdict(SortedList)
        ret = []
        for tr in transactions:
            n,t,a,c = tr.split(',')
            d[n].add((int(t), int(a), c))

        for k,l in d.items():
            i = 0
            f = set()
            for i in range(len(l)):
                if l[i][1] > 1000:
                    f.add(i)
                for j in range(i + 1, len(l)):
                    if l[j][0] - l[i][0] > 60:
                        break
                    if l[j][2] != l[i][2]:
                        f.add(i)
                        f.add(j)
            for i in f:
                ret.append(f'{k},{l[i][0]},{l[i][1]},{l[i][2]}')
        return ret
             
        
