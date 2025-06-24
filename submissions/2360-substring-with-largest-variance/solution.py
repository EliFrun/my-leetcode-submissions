class Solution:
    def largestVariance(self, s: str) -> int:
        ret = 0
        l = set(s)
        for c1 in l:
            for c2 in l:
                if c1 == c2:
                    continue
                count1, count2 = 0, 0
                left = 0
                seen = False
                for i in range(len(s)):
                    c = s[i]
                    if c not in (c1, c2):
                        continue
                    if c == c1:
                        count1 += 1
                        if count2 > 0:
                            ret = max(ret, count1 - count2)
                        elif seen:
                            ret = max(ret, count1 - count2 - 1)
                        continue
                    count2 += 1
                    seen = True
                    while count2 > count1:
                        if s[left] == c1:
                            count1 -= 1
                        elif s[left] == c2:
                            count2 -= 1
                        left += 1

                    ret = max(ret, count1 - count2)        
        return ret
                

        
