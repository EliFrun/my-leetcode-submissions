class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        ret = 0
        for k, v in c.items():
            ret += (k + 1) * ceil(v / (k + 1))

        return ret 
        
