class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:       
        bits = defaultdict(list)
        size = int(log2(max(arr) + 1) + 1)
        
        best = 0
        for i, num in enumerate(arr):
            best |= num
            j = 0
            while num > 0:
                if num & 1:
                    bits[j].append(i)
                j += 1
                num >>= 1


        ret = set()
        for i in range(len(arr)):
            curr_idx = i
            next_idx = i
            curr = 0
            while curr_idx < len(arr):
                curr |= arr[curr_idx]
                ret.add(curr)
                if curr == best:
                    break

                next_idx = len(arr)
                v = curr
                for j in range(size):
                    if v & 1:
                        v >>= 1
                        continue 
                    if (idx := bisect_left(bits[j], curr_idx)) < len(bits[j]) and bits[j][idx] > curr_idx:
                        next_idx = min(next_idx, bits[j][idx])
                    v >>= 1
                
                curr_idx = next_idx
        
        return len(ret)
            
            

        

        
        
