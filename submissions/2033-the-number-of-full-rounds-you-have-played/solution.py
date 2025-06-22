class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        sh, sm = int(loginTime.split(':')[0]), int(loginTime.split(':')[1])
        eh, em = int(logoutTime.split(':')[0]), int(logoutTime.split(':')[1])

        if sh < eh:
            return (60 - sm) // 15 + (eh - sh - 1) * 4 + em // 15
        elif sh == eh:
            if sm < em:
                return max(0, sum([1 if sm <= i <= em else 0 for i in range(0, 61, 15)]) - 1)
        return 4 * (23 - sh) + (60 - sm) // 15 + 4 * eh + em // 15
        
