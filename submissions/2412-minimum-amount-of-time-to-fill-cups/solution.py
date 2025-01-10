class Solution:
    def fillCups(self, cups: List[int]) -> int:
        cups.sort()
        ret = 0
        if cups[0] + cups[1] > cups[2]:
            targ = (cups[0] + cups[1] - cups[2] + 1) // 2
            return targ + cups[2]
        else:
            return cups[2]





    
        
