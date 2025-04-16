class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        start, end = 0, len(height) - 1
        currentMax = 0
        while(start < end):
            lmax = min( height[start], height[end]) * (end - start)
            currentMax = max(currentMax, lmax)
            if height[start] > height[end]:
                end -= 1
            elif height[start] < height[end]:
                start += 1
            else: 
                start += 1 
                end -= 1
                
        return currentMax
        
