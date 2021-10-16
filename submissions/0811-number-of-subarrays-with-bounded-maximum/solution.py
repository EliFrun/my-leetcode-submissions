class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        lists = [[]]
        for i in nums:
            if i > right:
                lists.append([])
            else:
                lists[-1].append(i)
            
        lists = [x for x in lists if x]
        
        def foo(l):
            if max(l) < left:
                return 0
            ret = 0
            i = 0
            while i < len(l):
                if l[i] >= left:
                    ret += len(l) - i
                else:
                    j = i
                    while j < len(l):
                        if l[j] < left:
                            j += 1
                        else:
                            ret += (j - i)*(len(l) - j)
                            i = j - 1
                            break
                i += 1
                        
            return ret
            
        
        ret = 0
        for l in lists:
            ret += foo(l)
            
        return ret
        
                
                
            
                    

        
        
