class Solution:
    def minPartitions(self, n: str) -> int:
        max_number = 0;
        for i in n:
            max_number = int(i) if int(i) > max_number else max_number
            
        return max_number
