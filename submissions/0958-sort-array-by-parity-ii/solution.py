class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = sorted([x for x in nums if x % 2 == 0])
        odd = sorted([x for x in nums if x % 2 != 0])
        
        ret = []
        for i in range(len(even)):
            ret.append(even[i])
            ret.append(odd[i])
            
        return ret
        
    
        
