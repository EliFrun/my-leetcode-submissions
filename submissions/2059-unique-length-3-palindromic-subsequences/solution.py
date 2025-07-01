class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = defaultdict(int)
        right = Counter(s)

        chars = defaultdict(set)
        for c in s:
            right[c] -= 1
            if right[c] == 0:
                right.pop(c)
            
            chars[c] |= set(right.keys()) & set(left.keys())
            left[c] += 1

        return sum([len(x) for x in chars.values()])

        
