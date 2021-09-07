class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m):
            current_pattern = arr[i: i + m]
            if self.lisEq(current_pattern, arr[i + m:i + 2 * m]):
                count = 1
                foo = arr[i + m:]
                while foo and count < k:
                    if self.lisEq(foo[:m], current_pattern):
                        count += 1
                    else:
                        break
                        
                    foo = foo[m:]
                    
                if count == k:
                    return True
                
        return False
    
    def lisEq(self, arr1, arr2):
        while arr1 and arr2:
            if arr1[0] != arr2[0]:
                return False
            
            arr1 = arr1[1:]
            arr2 = arr2[1:]
            
        return not arr1 and not arr2
