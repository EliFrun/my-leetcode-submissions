class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def solve(st):
            ret = 0
            if x > y:
                g = 'ab'
                b = 'ba'
            else:
                g = 'ba'
                b = 'ab'

            i = 0
            while i < len(st):
                if st[i: i + 2] == g:
                    ret += max(x,y)
                    st = st[:i] + st[i + 2:]
                    i -= 2
                i += 1
           
            i = 0
            while i < len(st):
                if st[i: i + 2] == b:
                    ret += min(x,y)
                    st = st[:i] + st[i + 2:]
                    i -= 2
                i += 1

            return ret


        curr = ""
        ret = 0
        for c in s:
            if c in 'ab':
                curr += c
            else:
                ret += solve(curr)
                curr = ""

        return ret + solve(curr)
        
