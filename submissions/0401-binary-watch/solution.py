class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    if j < 10:
                        j = f'0{j}'
                    ret.append(f'{i}:{j}')

        return ret
            

        
