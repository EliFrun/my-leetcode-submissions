class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        increasing_seq = 0
        for i in range(len(arr) - 1):
            if arr[i + 1] > arr[i]:
                increasing_seq += 1
            else:
                break

        decreasing_seq = 0
        for i in range(i, len(arr) - 1):
            if arr[i + 1] < arr[i]:
                decreasing_seq += 1
            else:
                break

        print(increasing_seq, decreasing_seq)
        return increasing_seq + decreasing_seq + 1 == len(arr) and increasing_seq > 0 and decreasing_seq > 0
                
        
