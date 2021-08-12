class Solution:
    def default():
        return 0
    
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        i = -1
        while(i < len(arr) - 1 and arr[i + 1] < 0):
            i += 1
        
        negative = []
        if i >= 0:
            negative = list(reversed(arr[:i  + 1]))
            if (i + 1) % 2 == 1:
                return False
        
        zeroes = []
        if i < len(arr) - 1 and arr[i + 1] == 0:
            start = i + 1
            while(i < len(arr) - 1 and arr[i + 1] == 0):
                i += 1
            zeroes = arr[start: i + 1]
        
        positive = arr[i + 1:] 
           
        foo = defaultdict(Solution.default)
        for i in arr:
            foo[i] += 1
             
        for i in negative:
            if i % 2 == 1:
                if 2 * i in foo:
                    if foo[2 * i] > 0:
                        foo[2 * i] -= 1
                    else:
                        return False
                else:
                    return False
            else:
                if i // 2 in foo and foo[i//2] > 0:
                    foo[i//2] -= 1
                elif 2 * i in foo and foo[2 * i] > 0:
                    foo[2 * i] -= 1
                else:
                    return False
            
        foo[0] = 0 if len(zeroes) % 2 == 0 else 1
            
        for i in positive:
            if i % 2 == 1:
                if 2 * i in foo:
                    if foo[2 * i] > 0:
                        foo[2 * i] -= 1
                    else:
                        return False
                else:
                    return False
            else:
                if i // 2 in foo and foo[i//2] > 0:
                    foo[i//2] -= 1
                elif 2 * i in foo and foo[2 * i] > 0:
                    foo[2 * i] -= 1
                else:
                    return False
                    
        print(foo)
        return all(v == 0 for v in foo.values())
