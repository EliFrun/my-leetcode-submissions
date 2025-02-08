class Solution:
    def countAndSay(self, n: int) -> str:
        curr = '1'
        for i in range(n - 1):
            nxt = ''
            cr = curr[0]
            count = 1
            for c in curr[1:]:
                if c == cr:
                    count += 1
                else:
                    nxt += str(count) + cr
                    cr = c
                    count = 1

            nxt += str(count) + cr
            curr = nxt

        return curr
        
