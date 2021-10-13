class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = sum(arr[:k])
        ret = 1 if curr >= k * threshold else 0
        for i in range(len(arr) - k):
            curr -= arr[i]
            curr += arr[i + k]
            ret += 1 if curr >= k * threshold else 0
            
        return ret
        
