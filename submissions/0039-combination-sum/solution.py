class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSumHelper(candidates, target)
        
        
        
    def combinationSumHelper(self, candidates: List[int], target: int) -> List[List[int]]:        
        ret = []
        for i in range(len(candidates)):
            if target - candidates[i] < 0:
                break
            elif target - candidates[i] == 0:
                ret += [[candidates[i]]]
                break
            else:
                for r in self.combinationSumHelper(candidates[i:], target - candidates[i]):
                    if r:
                        ret.append([candidates[i]] + r)   
        
        return ret
                 
            
        
