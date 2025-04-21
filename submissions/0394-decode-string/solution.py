class Solution:
    def decodeString(self, s: str) -> str:
        def solve(st):
            if not st:
                return ""
            if "[" not in st:
                return st

            i = 0
            while i < len(st):
                if st[i].isnumeric():
                    break
                i += 1
            k = i
            ret = st[:i]
            while i < len(st):
                if not st[i].isnumeric():
                    break
                i += 1
            num = st[k:i]
            l_count = 1
            r_count = 0
            j = i + 1
            while l_count > r_count:
                if st[j] == '[':
                    l_count += 1
                if st[j] == ']':
                    r_count += 1
                j += 1

            return ret + int(num) * solve(st[i + 1:j - 1]) + solve(st[j:])

        return solve(s)
