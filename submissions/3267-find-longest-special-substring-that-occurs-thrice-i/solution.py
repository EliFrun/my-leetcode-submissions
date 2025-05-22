class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(lambda: [0] * (len(s) + 1))
        left,right = 0, 0
        while right <= len(s):
            if right == len(s) or s[right] != s[left]:
                size = right - left
                for i in range(1, size + 1):
                    d[s[left]][i] += size - i + 1
                left = right
            right += 1

        print(d)
        ret = -1
        for l in d.values():
            for i in range(len(l)):
                if l[i] >= 3:
                    ret = max(ret, i)

        return ret
        
