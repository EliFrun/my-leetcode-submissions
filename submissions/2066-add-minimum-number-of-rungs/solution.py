class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        curr = 0
        curr_dis = 0
        ret = 0
        for curr in range(len(rungs)):
            if curr_dis + dist < rungs[curr]:
                ret += (rungs[curr] - curr_dis - 1)  // dist
                
            curr_dis = rungs[curr]
                    
        return ret
        
