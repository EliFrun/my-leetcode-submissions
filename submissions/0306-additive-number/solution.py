class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def solve(seq,  st):
            print(seq, st)
            if not st:
                return len(seq) > 2
            if st[0] == '0':
                if len(seq) > 1 and seq[-1] + seq[-2] == 0:
                    return solve(seq + [0], st[1:])
                elif len(seq) == 1:
                    return solve(seq + [0], st[1:])
                return False
            if len(seq) > 1:
                if int(st) == seq[-1] + seq[-2]:
                    return True
            for i in range(1,len(st)):
                for j in range(i + 1, len(st) + 1):
                    if seq[-1] + int(st[:i]) == int(st[i:j]) and st[i] != '0':
                        if solve(
                            seq + [int(st[:i]), int(st[i:j])],
                            st[j:]
                        ):
                            return True
            
            return False

        for i in range(1, len(num) if num[0] != '0' else 2):
            if solve([int(num[:i])], num[i:]):
                return True

        return False
            

        
