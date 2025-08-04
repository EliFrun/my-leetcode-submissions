class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        left = 0
        ret = 0
        for fruit in fruits:
            d[fruit] += 1
            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    d.pop(fruits[left])
                left += 1
            ret = max(ret, sum(d.values()))
        return ret


        
