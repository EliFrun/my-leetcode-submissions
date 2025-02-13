class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c = Counter(secret)
        bulls = 0
        for a,b in zip(secret, guess):
            if a == b:
                bulls += 1
                c[a] -= 1

        cows = 0
        for a,b in zip(secret, guess):
            if a != b:
                if c[b] > 0:
                    cows += 1
                    c[b] -= 1

        return f'{bulls}A{cows}B'
        
        
