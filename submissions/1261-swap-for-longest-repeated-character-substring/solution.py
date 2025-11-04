class Solution:
    def maxRepOpt1(self, text: str) -> int:
        lengths = []
        curr = ''
        cnt = 0
        counts = defaultdict(int)
        for c in text:
            counts[c] += 1
            if c == curr:
                cnt += 1
            else:
                lengths.append((curr, cnt))
                cnt = 1
                curr = c

        ret = 0
        lengths.append((curr, cnt))
        for i in range(len(lengths)):
            l, c = lengths[i]
            ret = max(ret, c)
            if counts[l] > c:
                ret = max(ret, c + 1)
            if i < len(lengths) - 2 and lengths[i + 1][1] == 1 and lengths[i + 2][0] == l:
                if c + lengths[i + 2][1] == counts[l]:
                    ret = max(ret, counts[l])
                else:
                    ret = max(ret, c + lengths[i + 2][1] + 1)

        return ret


        
