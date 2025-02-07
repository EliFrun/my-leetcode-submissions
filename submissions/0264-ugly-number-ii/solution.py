class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i = 1
        while i < n:
            l2 = [ x * 2 for x in nums if x * 2 > nums[-1] ]
            l3 = [ x * 3 for x in nums if x * 3 > nums[-1] ] 
            l5 = [ x * 5 for x in nums if x * 5 > nums[-1] ]
            nums.append(min(l2[0], l3[0], l5[0]))
            
            i += 1


        return nums[-1]
            

        
