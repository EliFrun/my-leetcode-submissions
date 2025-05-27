class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        d = {}
        ri, rj = -1, -1
        for i, v in reversed(list(enumerate(arr))):
            d[v] = i
            for k in range(v - 1, -1, -1):
                if k in d:
                    arr[i], arr[d[k]] = arr[d[k]], arr[i]
                    return arr
            
        return arr

        
