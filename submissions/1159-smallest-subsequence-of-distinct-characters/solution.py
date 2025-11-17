class Solution:
    def smallestSubsequence(self, s: str) -> str:
        needed = sorted(list(set(s)))
        ret = ''

        bitmask = 0
        for i in range(len(s) - 1, -1, -1):
            bitmask |= 1 << (ord(s[i]) - ord('a'))
        
        lower_bound = -1
        cnt = 0
        while needed:
            #print(ret, needed, bin(bitmask), lower_bound)
            cnt += 1
            if cnt > 26:
                break
            best_c = '{'
            best_idx = len(s)
            curr_bitmask = 0
            for i in range(len(s) - 1, lower_bound, -1):
                if bitmask & (1 << (ord(s[i]) - ord('a'))):
                    curr_bitmask |= 1 << (ord(s[i]) - ord('a'))
                    if curr_bitmask == bitmask:
                        if s[i] <= best_c:
                            best_c = s[i]
                            best_idx = i
            bitmask ^= 1 << (ord(best_c) - ord('a'))
            needed = [c for c in needed if c != best_c]
            ret += best_c
            lower_bound = best_idx

        return ret
                
                
            
                


        

        
