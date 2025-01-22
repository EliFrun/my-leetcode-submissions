class Solution:
    def numDecodings(self, s: str) -> int:

        @functools.cache
        def helper(st):         
            if  len(st) == 0:
                return 1

            if st[0] == '0':
                return 0

            if len(st) == 1:
                return 1
            
            tmp = 0
            if int(st[:2]) < 27:
                tmp = helper(st[2:])

            return helper(st[1:]) + tmp

        return helper(s)
        
