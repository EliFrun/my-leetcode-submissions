class Solution:
    def toHex(self, num: int) -> str:
        a = bin(num)[2:] if num >= 0 else bin(num & 0b11111111111111111111111111111111)[2:]
        ret = [[]]
        for i in reversed(list(a)):
            if len(ret[-1]) < 4:
                ret[-1].append(i)
            else:
                ret.append([i])
        
         
        def remove0s(a):
            for i in range(len(a)):
                if a[i] == '1':
                    return a[i:]
            return ''
        
        def tohex(a):
            return {
                ''    : '0',
                '1'   : '1',
                '10'  : '2',
                '11'  : '3',
                '100' : '4',
                '101' : '5',
                '110' : '6',
                '111' : '7',
                '1000': '8',
                '1001': '9',
                '1010': 'a',
                '1011': 'b',
                '1100': 'c',
                '1101': 'd',
                '1110': 'e',
                '1111': 'f'
            }[a]
        
        return ''.join(
            reversed(
                [
                    tohex(
                        remove0s(
                            "".join(
                                reversed(x)
                            )
                        )
                    ) for x in ret
                ]
            )
        )
        
            
        
        
