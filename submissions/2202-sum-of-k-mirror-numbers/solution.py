class Solution:
    def kMirror(self, k: int, n: int) -> int:
        @cache
        def generate_num(left, first):
            if left == 1:
                return [str(i) for i in range(1 if first else 0, k)]
            ret = []
            for i in range(1 if first else 0, k):
                ret.extend([str(i) + x for x in generate_num(left - 1, False)])
            return ret
        
        def generate_palindrome(l):
            ret = []
            if l == 1:
                return [str(x) for x in range(1, k)]
            for left in generate_num(l//2, True):
                if l & 1:
                    for i in range(k):
                        ret.append(left + str(i) + left[::-1])
                else:
                    ret.append(left + left[::-1])
            return ret


        l = 1
        found = 0
        ret = 0
        while found < n:
            nums = generate_palindrome(l)
            for v in nums:
                if found >= n:
                    break
                if str(int(v, k)) == str(int(v, k))[::-1]:
                    #print(v, int(v,k))
                    ret += int(v, k)
                    found += 1
            l += 1

        return ret


            
                    


        
