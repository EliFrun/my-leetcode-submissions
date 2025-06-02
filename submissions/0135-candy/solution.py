class Solution:
    def candy(self, ratings: List[int]) -> int:
        ret = 1
        dec, inc = 1, 1
        prev = 0
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                dec = 1
                inc += 1
                prev = inc
                ret += inc
            elif ratings[i] > ratings[i + 1]:
                inc = 1
                if dec >= prev:
                    ret += 1
                ret += dec
                dec += 1
            else:
                ret += 1
                prev = 1
                dec = 1
                inc = 1

        return ret

            

        

            
        
