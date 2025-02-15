class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        ret = []
        for x in arr2:
            ret += [x] * c[x]
            c[x] = 0

        for k,v in sorted([(k,v) for k,v in c.items() if v > 0]):
            ret += [k] * v
            

        return ret

        

        
