class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern = pattern

        ret = []
        m = 1
        d_count = 0
        k = 0
        while k < len(pattern):
            #print(pattern, m, d_count, ret)
            if pattern[k] == 'I':
                ret.append(m + d_count)
                for i in range(m + d_count - 1, m - 1, -1):
                    ret.append(i)
                m = m + d_count + 1
                d_count = 0

            else:
                d_count += 1
            k += 1

        ret.append(m + d_count)
        for i in range(m + d_count - 1, m - 1, -1):
            ret.append(i)

        return ''.join([str(x) for x in ret])
            
        
