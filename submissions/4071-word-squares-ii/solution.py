class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def solve(prev):
            if len(prev) == 1:
                ret = [solve(prev + [word]) for word in words if word != prev[0] and word[0] == prev[0][0]]
                l = []
                for lis in ret:
                    l += lis
                return l
            if len(prev) == 2:
                ret = [solve(prev + [word]) for word in words if word not in prev and word[0] == prev[0][3]]
                l = []
                for lis in ret:
                    l += lis
                return l
            if len(prev) == 3:
                ret = [prev + [word] for word in words if word not in prev and word[0] == prev[1][3] and word[3] == prev[2][3]]
                return ret


        ret = []
        for word in words:
            ret.extend([x for x in solve([word]) if len(x) == 4])
        ret.sort()
        return ret
                
                
        
