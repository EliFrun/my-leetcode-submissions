class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        m = {
            5: 0,
            10: 0,
            20: 0
        }
        
        for bill in bills:
            if bill == 5:
                m[5] += 1
            if bill == 10:
                if m[5] > 0:
                    m[10] += 1
                    m[5] -= 1
                else:
                    return False
            if bill == 20:
                if (m[5] > 0 and m[10] > 0) or m[5] >= 3:
                    if m[10] > 0:
                        m[10] -= 1
                        m[5] -= 1
                    elif m[5] >= 3:
                        m[5] -= 3
                else:
                    return False
                
        return True
