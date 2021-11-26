class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
       
        ret = 0
        curr = 0
        state = 0
        for i in range(len(arr)):
            if i == len(arr) - 1:
                if state >= 0:
                    break
                else:
                    ret = max(ret, curr)
                    break
            if state == 0:
                if arr[i + 1] <= arr[i]:
                    continue
                else:
                    state = 1
                    curr = 0
            
            if state == 1:
                if arr[i + 1] < arr[i]:
                    state = -1
                    curr += 1
                elif arr[i + 1] == arr[i]:
                    state = 0
                    curr = 0
                else:
                    curr += 1
                    
            if state == -1:
                if arr[i + 1] > arr[i]:
                    state = 1
                    ret= max(ret, curr)
                    curr = 1
                elif arr[i + 1] == arr[i]:
                    state = 0
                    ret = max(ret, curr)
                    curr = 0
                else:
                    curr += 1
                    
                    
        return ret
