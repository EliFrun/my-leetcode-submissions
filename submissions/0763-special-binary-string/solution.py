def gt(a, b):
    return a + b > b + a
    
def ms(l):
    if not l:
        return []
    if len(l) == 1:
        return l
    if len(l) == 2:
        if gt(l[0], l[1]):
            return l
        return l[::-1]
    l1 = ms(l[0:len(l)//2])
    l2 = ms(l[len(l)//2:])
    ret = []
    while l1 or l2:
        if l1 and l2:
            if gt(l1[0], l2[0]):
                ret.append(l1.pop(0))
            else:
                ret.append(l2.pop(0))
        elif l1:
            ret.append(l1.pop(0))
        else:
            ret.append(l2.pop(0))
    return ret

class Solution:
    def makeLargestSpecial(self, st: str) -> str:
        @cache
        def solve(s):
            if not s:
                return s
            l = [0]
            for c in s:
                l.append(l[-1] + (1 if c == '1' else -1))
            l = l[1:]
            vals = [x for x in sorted(list(set(l))) if x >= 0]
            
            ret = s
            for val in vals:
                cnt = [0,0]
                lis = []
                curr = ''
                for i, c in enumerate(s):
                    if l[i] < val:
                        lis.append(curr + c)
                        curr = ''
                    else:
                        curr += c
                        if curr.count('0') == curr.count('1'):
                            lis.append(curr)
                            curr = ''
                lis = [x if x.count('1') != x.count('0') or len(x) == len(s) else solve(x) for x in lis]
                print(s, lis)
                ll = []
                v = []
                for ss in lis:
                    if ss.count('0') != ss.count('1'):
                        v.extend(ms(ll))
                        v.append(ss)
                        ll = []
                    else:
                        ll.append(ss)
                v.extend(ms(ll))
                    
            
                ret = max(ret, ''.join(v))
            return ret
        return solve(st)

                        
        
