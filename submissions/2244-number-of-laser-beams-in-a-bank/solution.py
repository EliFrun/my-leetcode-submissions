class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ret = 0
        prev = 0
        for row in bank:
            if (v := row.count('1')) > 0:
                ret += prev * v
                prev = v

        return ret
        
