class Solution:
    def stringHash(self, s: str, k: int) -> str:
        substrings = []
        curr = ""
        for c in s:
            curr = curr + c
            if len(curr) == k:
                substrings.append(curr)
                curr = ""
        

        def solve(st):
            return chr(ord('a') + sum([ord(c) - ord('a') for c in st]) % 26)

        return ''.join([solve(x) for x in substrings])
        
