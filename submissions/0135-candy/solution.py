class Solution:
    def candy(self, ratings: List[int]) -> int:
        ret = 1
        curr = 1
        chain = 1
        prev_val = 0
        print(f'curr: {curr}')
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                chain = 0
                curr += 1
                prev_val = curr
            elif ratings[i] == ratings[i - 1]:
                chain = 0
                curr = 1
                prev_val = curr
            else:
                if chain == prev_val - 1:
                    chain += 1
                curr = 1
                ret += chain
                chain += 1
                print(f'chain: {chain}')
            ret += curr
            print(f'curr: {curr}')


        return ret

        

            
        
