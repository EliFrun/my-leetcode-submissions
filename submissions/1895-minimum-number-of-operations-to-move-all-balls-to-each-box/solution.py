class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        s = set()
        
        for i, v in enumerate(boxes):
            if v == "1":
                s.add(i)
                
        ret = [0] * len(boxes)
        
        for i in s:
            for j in range(len(ret)):
                ret[j] += abs(j - i)
                
        return ret
        
