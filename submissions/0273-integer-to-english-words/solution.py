class Solution:
    def numberToWords(self, num: int) -> str:
        billion = num // 10 ** 9
        num = num % 10 ** 9
        million = num // 10 ** 6
        num = num % 10 ** 6
        thousand = num // 10 ** 3
        num = num % 10 ** 3
        hundred = num
        
        ret = ""
        if billion:
            ret += self.convertToWord(billion) + "Billion "
        if million:
            ret += self.convertToWord(million) + "Million "
        if thousand:
            ret += self.convertToWord(thousand) + "Thousand "
        if hundred:
            ret += self.convertToWord(hundred)
            
        return ret[:-1] if ret else "Zero"
        
        
        
    def convertToWord(self, num):
        digits = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
        t = {
            1: "Ten",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        teens = {
            0: "Ten",
            1: "Eleven",
            2: "Twelve",
            3: "Thirteen",
            4: "Fourteen",
            5: "Fifteen",
            6: "Sixteen",
            7: "Seventeen",
            8: "Eighteen",
            9: "Nineteen"
        }
        hundreds = num // 100
        num = num % 100
        tens = num // 10
        num = num % 10
        one = num
        
        ret = ""
        if hundreds:
            ret += f'{digits[hundreds]} Hundred '
        if tens:
            if 1 == tens:
                ret += f'{teens[one]} '
                return ret
            else:
                ret += f'{t[tens]} '
        if one:
            ret += f'{digits[one]} '
            
        return ret
