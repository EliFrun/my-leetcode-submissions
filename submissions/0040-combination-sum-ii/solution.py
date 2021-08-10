class Solution:
    def default():
        return 0
    
    def bigger(self, a: List[int],b: List[int]) -> bool: # a > b ?
        for i in range(min(len(a), len(b))):
            if a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False 
        return False
        
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        
        candidates.sort()
        s = defaultdict(Solution.default)
        for i in candidates:
            s[i] += 1
        st = []   
        for key, value in s.items():
            st += [key] * min(value, target // key)
        candidates = st
        
        
        tmp = self.combinationSumHelper(candidates, target)
        if not tmp:
            return []
        
        current_max = tmp[0]
        ret = [tmp[0]]
        for t in tmp:
            if self.bigger(t, current_max):
                ret.append(t)
                current_max = t
        return ret

        
    def combinationSumHelper(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        ret = []
        for i in range(len(candidates)):
            if sum(candidates[i:]) < target:
                break
            if target - candidates[i] < 0:
                break
            elif target - candidates[i] == 0:
                ret += [[candidates[i]]]
                break
            else:
                for r in self.combinationSumHelper(candidates[i + 1:], target - candidates[i]):
                    if r:
                        ret.append([candidates[i]] + r)
        
        return ret
        
