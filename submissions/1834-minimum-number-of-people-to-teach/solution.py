class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        @cache
        def helper(u,v):
            return languages[u] & languages[v]
        
        for i in range(len(languages)):
            languages[i] = set(languages[i])

        languages = [[]] + languages

        m = max([max(x) for x in friendships])
        ret = float('inf')
        for j in range(n + 1):
            val_set = [False] * (m + 1)
            for u,v in friendships:
                if helper(u,v):
                    continue
                if val_set[u] and val_set[v]:
                    continue
                if val_set[u] and j in languages[v]:
                    continue
                if val_set[v] and j in languages[u]:
                    continue
                if j not in languages[u]:
                    val_set[u] = True
                if j not in languages[v]:
                    val_set[v] = True
                

            ret = min(ret, len([x for x in val_set if x]))
        return ret

        
