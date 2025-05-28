class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ret = [0] * num_people
        i = 0
        while candies > 0:
            if i >= candies:
                ret[i% len(ret)] += candies
                break
            ret[i% len(ret)] += (i + 1)
            candies -= i + 1
            i += 1

        return ret


        
