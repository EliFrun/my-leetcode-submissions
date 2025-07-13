class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        for i in range(12):
            cnt = bin(i).count('1')
            for j in range(60):
                if bin(j).count('1') + cnt == turnedOn:
                    j = ('0' if j < 10 else '') + str(j)
                    ret.append(f'{i}:{j}')

        return ret
        
