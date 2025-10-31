class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        l1, l2, l3 = set(), set(), set()

        for w, l in matches:
            if w not in l2 and w not in l3: l1.add(w)
            
            if l in l1:
                l1.remove(l)
                l2.add(l)
            elif l in l2:
                l2.remove(l)
                l3.add(l)
            elif l in l3:
                continue
            else:
                l2.add(l)

        return [sorted(list(l1)), sorted(list(l2))]
        
