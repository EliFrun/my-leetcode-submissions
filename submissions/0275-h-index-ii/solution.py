class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start, end = 0, len(citations) - 1
        while end - start > 1:
            mid = (start + end) // 2
            if len(citations) - mid >= citations[mid]:
                start = mid
            elif len(citations) - mid < citations[mid]:
                end = mid

        if len(citations) - start <= citations[start]:
            return len(citations) - start
        if len(citations) - end <= citations[end]:
            return len(citations) - end
        return 0
        
