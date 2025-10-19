class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        def solve(strict, counts):
            idx = len(s) - sum(counts)
            if idx == len(s) - 1:
                if strict:
                    if ord(target[-1]) - ord('a') < counts.index(1):
                        return chr(ord('a') + counts.index(1))
                    else:
                        return ''
            ret = ''
            for i in range(len(counts)):
                c = chr(ord('a') + i)
                if counts[i] == 0:
                    continue
                if strict:
                    v = ''
                    if c < target[idx]:
                        continue
                    elif c == target[idx]:
                        v = solve(True, tuple([x if ii != i else x - 1 for ii, x in enumerate(counts)]))
                    else:
                        v = solve(False, tuple([x if ii != i else x - 1 for ii, x in enumerate(counts)]))
                    if v:
                        ret = c + v
                        break
                else:
                    ret = c + solve(False, tuple([x if ii != i else x - 1 for ii, x in enumerate(counts)]))
                    break
            return ret

        c = Counter(s)
        l = [c[chr(ord('a') + i)] for i in range(26)]
        return solve(True, l)
        
