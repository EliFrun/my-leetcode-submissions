class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        vals = sorted([[a, 'a'],[b, 'b'], [c, 'c']])
        if vals[-1][0] > 2 * sum([ x for x,y in vals[:2]]) + 2:
            ret = ''
            for i in range(3 * sum([ x for x,y in vals[:2]]) + 2):
                if ((i + 1) % 3) == 0:
                    if vals[0][0] > 0:
                        vals[0][0] -= 1
                        ret += vals[0][1]
                    else:
                        ret += vals[1][1]
                else:
                    ret += vals[2][1]      
            return ret
        else:
            ret = []
            while any([x > 0 for x,y in vals[:2]]):
                ret += [[vals[2][1]]]
                ret += [[vals[0][1] if vals[0][0] > 0 else vals[1][1]]]
                
                vals[2][0] -= 1
                if vals[0][0] > 0:
                    vals[0][0] -= 1
                else:
                    vals[1][0] -= 1
                    
                vals.sort()
                    
                    
            if any([x > 0 for x,y in vals]):
                for val in vals:
                    if val[0] < 1:
                        continue
                    for lis in ret:
                        if val[0] < 1:
                            break
                        if lis[0] != val[1]:
                            continue
                        if len(lis) > 1:
                            continue
                        else:
                            lis.append(val[1])
                            val[0] -= 1
                            
            
            if vals[2][0] > 0:
                ret.append([vals[2][1] * vals[2][0]])
            ret_string = ''
            
            for lis in ret:
                for c in lis:
                    ret_string += c
                    
            return ret_string
            
            
            
        
