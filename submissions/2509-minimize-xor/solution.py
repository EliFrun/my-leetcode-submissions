class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_str = "{0:b}".format(num1)
        num2_str = "{0:b}".format(num2)

        if len(num1_str) > len(num2_str):
            num2_str = '0' * (len(num1_str) - len(num2_str)) + num2_str

        if len(num2_str) > len(num1_str):
            num1_str = '0' * (len(num2_str) - len(num1_str)) + num1_str

        print(num1_str)
        print(num2_str)

        target = num2_str.count('1')

        def solve(s, count):
            if count == target:
                return s

            if count > target:
                if s[-1] == '1':
                    return solve(s[:-1], count - 1) + '0'
                return solve(s[:-1], count) + '0'
            elif count < target:
                if s[-1] == '1':
                    return solve(s[:-1], count) + '1'
                return solve(s[:-1], count + 1) + '1'

            


        return  int(''.join(solve(num1_str, num1_str.count('1'))), 2)

            


        
