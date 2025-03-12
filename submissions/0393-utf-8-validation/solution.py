class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def bin_1(n):
            return "{0:8b}".format(n).replace(' ', '0')
        i = 0
        while i < len(data):
            num = data[i]
            if str(bin_1(num)).startswith('11110'):
                if i + 3 >= len(data):
                    return False
                if not bin_1(data[i + 1]).startswith('10'):
                    return False
                if not bin_1(data[i + 2]).startswith('10'):
                    return False
                if not bin_1(data[i + 3]).startswith('10'):
                    return False
                i += 4
            elif bin_1(num).startswith('1110'):
                if i + 2 >= len(data):
                    return False
                if not bin_1(data[i + 1]).startswith('10'):
                    return False
                if not bin_1(data[i + 2]).startswith('10'):
                    return False
                i += 3
            elif bin_1(num).startswith('110'):
                if i + 1 >= len(data):
                    return False
                if not bin_1(data[i + 1]).startswith('10'):
                    return False
                i += 2
            elif bin_1(num).startswith('0'):
                i += 1
            else:
                return False

        return True
                
