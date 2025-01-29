class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        sets = []

        for n1, n2 in edges:
            candidate_sets = []
            for i in range(len(sets) - 1, -1, -1):
                if n1 in sets[i] or n2 in sets[i]:
                    candidate_sets.append(sets.pop(i))
            if len(candidate_sets) == 0:
                sets.append(set([n1, n2]))
            if len(candidate_sets) == 1:
                if n1 in candidate_sets[0] and n2 in candidate_sets[0]:
                    return [n1, n2]
                candidate_sets[0].add(n1)
                candidate_sets[0].add(n2)
                sets.append(candidate_sets[0])

            if len(candidate_sets) == 2:
                sets.append(candidate_sets[0].union(candidate_sets[1]))

        
        return edges[-1]

            
        
