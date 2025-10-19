class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        offsets = set()
        curr = a
        while curr not in offsets:
            offsets.add(curr)
            curr = (curr + a) % 10

        def best(seq):
            v = int(seq[0])
            offset = -1
            best = 10
            for o in offsets:
                if (v + o) % 10 < best:
                    best = (v + o) % 10
                    offset = o
            return ''.join([str((int(x) + offset) % 10) for x in seq])
            

    
        
        # if diff_parity, all values can undergo the first transform
        diff_parity = b % 2 == 1

        possible_starts = set()
        curr = 0
        while curr not in possible_starts:
            possible_starts.add(curr)
            curr = (curr - b + len(s)) % len(s)

        ret = '9' * len(s)
        for p in possible_starts:
            st = s[p:] + s[:p]
            odds = best(''.join(c for i, c in enumerate(st) if i & 1))
            evens = ''.join(c for i, c in enumerate(st) if not i & 1)
            if diff_parity:
                evens = best(evens)
            curr = ''
            for e,o in zip(evens, odds):
                curr += f'{e}{o}'
            ret = min(ret, curr)
        return ret


        
        
        

            
        

                
                

        
