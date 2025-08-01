class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for word in words:
            v = prefix[-1]
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                v += 1
            prefix.append(v)

        return [prefix[r + 1] - prefix[l] for l, r in queries]
        
