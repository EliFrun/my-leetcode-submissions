class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knows = set([0, firstPerson])
        meetings.sort(key=lambda x: x[2])
        meetings.append([0,0,float('inf')])
        parents = list(range(n))

        def union(x,y):
            x = find(x)
            y = find(y)
            if x != y:
                parents[x] = y

        def find(x):
            if parents[x] != x:
                p = find(parents[x])
                parents[x] = p
            return parents[x]
    
        curr = -1
        people = set()
        for x, y, t in meetings:
            if t != curr:
                groups = defaultdict(set)
                knows_secret = set()
                for p in people:
                    if p in knows:
                        knows_secret.add(find(p))
                    groups[find(p)].add(p)

                for k, v in groups.items():
                    if k in knows_secret:
                        knows.update(v)

                for p in people:
                    parents[p] = p
                curr = t
                people = set()
            people.update([x,y])
            union(x,y)
        return sorted(list(knows))


        
