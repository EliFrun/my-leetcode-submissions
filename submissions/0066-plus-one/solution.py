class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i >= 0 and carry == 1:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i -= 1

        if carry == 1:
            digits = [1] + digits
        return digits
        
