class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        dis = 0
        for i, (ca, cb) in enumerate(zip(a,b[::-1])):
            if i >= len(a) // 2:
                dis = i
                break
            if ca != cb:
                dis = i
                break
        s = a[:len(a) - dis] + b[len(b) - dis:len(b)]
        if s == s[::-1]:
            return True
        
        s = a[:dis] + b[dis:]
        if s == s[::-1]:
            return True

        dis = 0
        for i, (ca, cb) in enumerate(zip(a[::-1],b)):
            if i >= len(a) // 2:
                dis = i
                break
            if ca != cb:
                dis = i
                break
        s = b[:len(b) - dis] + a[len(a) - dis:len(a)]
        if s == s[::-1]:
            return True
        
        s = b[:dis] + a[dis:]
        if s == s[::-1]:
            return True
        return False

            
        
