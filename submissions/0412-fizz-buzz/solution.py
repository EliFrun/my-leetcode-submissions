class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for i in range(1, n + 1):
            p = ""
            if i % 3 == 0:
                p += 'Fizz'
            if i % 5 == 0:
                p += 'Buzz'
                
            ret.append(p if p else str(i))
            
        return ret
