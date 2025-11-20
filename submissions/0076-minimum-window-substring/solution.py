class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        ret = ''
        cs = defaultdict(int)
        below = set(c.keys())

        left, right = 0, 0
        while right < len(s):
            cs[s[right]] += 1
            if s[right] in below and cs[s[right]] >= c[s[right]]:
                below.remove(s[right])
            while not below:
                if not ret or right - left + 1 < len(ret):
                    ret = s[left: right + 1]
                cs[s[left]] -= 1
                if cs[s[left]] < c[s[left]]:
                    below.add(s[left])
                left += 1
            right += 1
        
        return ret
            
            
        
        
