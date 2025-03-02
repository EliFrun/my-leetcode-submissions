class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1 == 1:
            return False
        
        free = []
        lock = []
        for i, (c, l) in enumerate(zip(s, locked)):
            if l == '0':
                free.append(i)
            else:
                if c == '(':
                    lock.append(i)
                else:
                    if lock:
                        lock.pop()
                    elif free:
                        free.pop()
                    else:
                        return False

        while lock:
            if free and lock and free[-1] > lock[-1]:
                lock.pop()
                free.pop()
            else:
                return False
        return len(free) & 1 == 0
        
