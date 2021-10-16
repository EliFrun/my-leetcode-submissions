class Solution:
    def reorganizeString(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
            
        if any([x > (len(s)+ 1)//2 for x in d.values()]):
            return ""
        
        char_count = sorted(d.items(), key= lambda x: -x[1])
        ret = [""] * len(s)
        curr_location = 0
        for c, count in char_count:
            for i in range(count):
                if curr_location >= len(s):
                    curr_location = 1
                ret[curr_location] = c
                curr_location += 2
                
        return "".join(ret)
            
