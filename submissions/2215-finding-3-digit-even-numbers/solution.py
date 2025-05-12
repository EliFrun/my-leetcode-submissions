class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        c = Counter(digits)
        ret = []
        for i in range(1,10):
            for j in range(10):
                for k in range(0, 10, 2):
                    d = Counter([i,j,k])
                    if any(c.get(key, 0) < v for key, v in d.items()):
                        continue
                    ret.append(int(f'{i}{j}{k}'))

        return ret
                    



        
