class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        groups = []
        for c1, c2 in zip(s1, s2):
            g1, g2 = -1, -1
            for i, group in enumerate(groups):
                if c1 in group:
                    g1 = i
                if c2 in group:
                    g2 = i

            if g1 == g2:
                if g1 >= 0:
                    continue
                else:
                    groups.append(set([c1, c2]))
            else:
                if g1 >= 0 and g2 >= 0:
                    g1, g2 = groups.pop(max(g1, g2)), groups.pop(min(g1, g2))
                    groups.append(g1 | g2)
                elif g1 == -1:
                    groups[g2].add(c1)
                elif g2 == -1:
                    groups[g1].add(c2)
        groups = [sorted(list(x)) for x in groups]
        
        ret = list(baseStr)
        for i in range(len(ret)):
            for group in groups:
                if ret[i] in group:
                    ret[i] = group[0]
                    break
        return ''.join(ret)

        
