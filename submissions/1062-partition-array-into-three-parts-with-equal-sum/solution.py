class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        a = sum(arr)
        if not a % 3 == 0:
            return False
        else:
            d = a // 3
            for _ in range(3):
                if not arr:
                    return False
                if _ == 2:
                    if sum(arr) == d:
                        arr = []
                        a -= d
                else:
                    foo = 0
                    for i, v in enumerate(arr):
                        foo += v
                        if foo == d:
                            a -= foo
                            arr = arr[i + 1:]
                            break
            
            return (not arr) and a == 0
                    
            
            
            
