class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        tree = [[] for _ in range(len(favorite))]
        for i, v in enumerate(favorite):
            tree[v].append(i)

        two_cycles = []
        in_two_cycle = [False] * len(favorite)
        for i,v in enumerate(favorite):
            if in_two_cycle[i]:
                continue
            if favorite[v] == i:
                two_cycles.append((i,v))
                in_two_cycle[i] = True
                in_two_cycle[v] = True

        in_a_cycle = set()
        best_depth = []
        for l, r in two_cycles:
            curr = set([l])
            depth = -1
            while curr:
                nxt = set()
                depth += 1
                for i in curr:
                    in_a_cycle.add(i)
                    nxt.update([x for x in tree[i] if x != r])
                curr = nxt
            
            best_depth.append(depth)

            curr = set([r])
            depth = -1
            while curr:
                nxt = set()
                depth += 1
                for i in curr:
                    in_a_cycle.add(i)
                    nxt.update([x for x in tree[i] if x != l])
                curr = nxt
            best_depth.append(depth)

        best_2_cycle = 2 * len(two_cycles) + sum(sorted(best_depth, reverse=True)[:2 * len(two_cycles)])

        best_cycle = 0
        traversed = set()
        for i, v in enumerate(favorite):
            if i in in_a_cycle:
                continue
            found = {}
            layer = 0
            j = i
            pathfinder = []
            already_seen = False
            while j not in found:
                if j in traversed:
                    already_seen = True
                    break
                traversed.add(j)
                found[j] = layer
                pathfinder.append(j)
                j = favorite[j]
                layer += 1

            if not already_seen:
                best_cycle = max(best_cycle, layer - found[j])

        return max(best_2_cycle, best_cycle)

        


        

            





            


        
        
