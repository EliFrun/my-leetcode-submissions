class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, j = 0, 0
        max_len = 0
        d = defaultdict(int)
        while j < len(fruits):
            d[fruits[j]] += 1
            while len(d) > 2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    d.pop(fruits[i])
                i += 1
                
            max_len = max(max_len, j - i)
            j += 1
        
        return max_len + 1
