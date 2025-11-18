class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] != 0:
            return False
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            elif i <= len(bits) - 2 and bits[i] == 1 and bits[i] in [0,1]:
                i += 2
            else:
                return False
        return i != len(bits) and bits[i] == 0
        
