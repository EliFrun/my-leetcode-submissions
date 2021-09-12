class Solution:
    def primePalindrome(self, n: int) -> int:
        if self.isPal(n) and self.isPrime(n):
            return n
        foo = self.nextPalindrome(n)
        while not self.isPrime(foo):
            foo = self.nextPalindrome(foo)
            
        return foo
       
    def isPal(self, n):
        foo = str(n)
        for i in range(len(foo) // 2):
            if foo[i] != foo[-1 - i]:
                return False
            
        return True
    
    def nextPalindrome(self, n):
        a = str(n)
        if len(a) % 2 == 0:
            foo = a[:len(a)//2]
            b = int(foo + foo[::-1])
            if b > n:
                return b
            else:
                foo = int(foo)
                while int(str(foo) + str(foo)[::-1]) <= n:
                    foo += 1
                    if foo == 10 ** (len(a) // 2):
                        return int(str(foo) + str(foo)[:len(a) // 2][::-1])
                return int(str(foo) + str(foo)[::-1])
        else:
            foo = a[:len(a)//2 + 1]
            b = int(foo + str(foo)[:len(a) // 2][::-1])
            if b > n:
                return b
            else:
                foo = int(foo)
                while int(str(foo) + str(foo)[:len(a) // 2][::-1]) <= n:
                    foo += 1
                    if foo == 10 ** (len(a) // 2 + 1):
                        return int(str(foo)[:-1] + str(foo)[:-1][::-1])
                return int(str(foo) + str(foo)[:len(a) // 2][::-1])
            
    
    def isPrime(self, n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
            
        return True
        
