class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        expires_at = timeSeries[0] + duration
        total = 0
        for i in timeSeries[1:]:
            if expires_at < i:
                total += duration
                
            if expires_at >= i:
                total += i - expires_at + duration
                
            expires_at = i + duration
        total += duration
            
        return total
