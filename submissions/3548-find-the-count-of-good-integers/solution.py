class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def even_counter():
            seen = set()
            ret = 0
            for i in range(10**(n//2 - 1), 10**(n//2)):
                serial = tuple(sorted(list(str(i))))
                if serial in seen:
                    continue
                
                if int(str(i) + str(i)[::-1]) % k != 0:
                    continue
    
                seen.add(serial)

                c = Counter(serial)
                combos = (n - 2 * c.get('0', 0)) * factorial(n - 1)
                for _,v in c.items():
                    combos //= factorial(2 * v)

                ret += combos
            return ret

        def odd_counter():
            ret = 0
            for j in range(10):
                if n == 1:
                    ret += 1 if j % k == 0 and j != 0 else 0
                    continue
                seen = set()
                for i in range(10**(n//2 - 1), 10**(n//2)):
                    serial = tuple(sorted(list(str(i))))
                    if serial in seen:
                        continue
                    
                    if int(str(i) + str(j) + str(i)[::-1]) % k != 0:
                        continue
        
                    seen.add(serial)

                    c = Counter(serial)
                    combos = (n - 2 * c.get('0', 0) - (1 if j == 0 else 0)) * factorial(n - 1)
                    for key,v in c.items():
                        combos //= factorial(2 * v + (1 if key == str(j) else 0))

                    ret += combos
            return ret



        return odd_counter() if n & 1 == 1 else even_counter()      
