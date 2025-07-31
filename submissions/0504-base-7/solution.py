class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = "" if num >= 0 else "-"
        ret = ""
        num = abs(num)
        while num:
            ret += str(num % 7)
            num //= 7
        if not ret:
            ret = "0"

        return sign + ret[::-1]
