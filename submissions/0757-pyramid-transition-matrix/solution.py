class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        pattern_map = defaultdict(set)
        for s in allowed:
            pattern_map[s[:2]].add(s[2])

        @cache
        def solve(layer):
            if len(layer) == 1:
                return True
            combos = set([''])
            for i in range(len(layer) - 1):
                nxt = set()
                for s in pattern_map[layer[i:i + 2]]:
                    for c in combos:
                        nxt.add(c + s)
                combos = nxt
            
            for combo in combos:
                if len(combo) < len(layer) - 1:
                    continue
                if solve(combo):
                    return True
            return False

        return solve(bottom)


        
