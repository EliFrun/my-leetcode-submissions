class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def solve(w):
            if len(w) == 1:
                return w[0]
            
            w = list(w)
            combos = []
            for i in range(len(w)):
                for j in range(len(w)):
                    if i == j:
                        continue
                    for k in range(min(len(w[i]), len(w[j])) - 1, -1, -1):
                        if w[i][len(w[i]) - k:] == w[j][:k]:
                            if len(combos) < 2:
                                heappush(combos, (k, (i, j), w[i] + w[j][k:]))
                            elif len(combos) > 1 and k > combos[0][0]:
                                heappop(combos)
                                heappush(combos, (k, (i, j), w[i] + w[j][k:]))
                            break


            w1 = deepcopy(w)
            w1.pop(max(combos[1][1]))
            w1.pop(min(combos[1][1]))
            s1 = solve(tuple(sorted(w1 + [combos[1][2]])))
            
            w2 = deepcopy(w)
            w2.pop(max(combos[0][1]))
            w2.pop(min(combos[0][1]))
            s2 = solve(tuple(sorted(w2 + [combos[0][2]])))
            if len(s2) < len(s1):
                return s2
            return s1
        return solve(tuple(sorted(words)))       
        
