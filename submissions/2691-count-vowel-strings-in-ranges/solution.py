class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0]
        for s in words:
            if s[0] in 'aeiou' and s[-1] in 'aeiou':
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1])
        
        prefix_sum = prefix_sum
        return [prefix_sum[j + 1] - prefix_sum[i] for i,j in queries]
        
