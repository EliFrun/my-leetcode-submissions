class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            return int("".join(reversed(str(num))))
        
        
            
        reverse_index = defaultdict(int)
        for i, v in enumerate(nums):
            reverse_index[v - rev(v)] += 1
            
        ret = 0
        for _, v in reverse_index.items():
            ret += (v * (v - 1)) // 2
            
        return ret % 1_000_000_007
      

        
