class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = defaultdict(list)
        for i,v in enumerate(list1):
            d[v].append(i)
        
        for i,v in enumerate(list2):
            d[v].append(i)

        m = float('inf')
        ret = []
        for k, v in d.items():
            if len(v) == 1:
                continue
            if sum(v) == m:
                ret.append(k)
            elif sum(v) < m:
                m = sum(v)
                ret = [k]

        return ret


        

        
