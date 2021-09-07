class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d = {}
        #allowed = ["".join(sorted(list(x))) for x in allowed]
        f = defaultdict(lambda: defaultdict(set))
        for a in allowed:
            f[a[0]][a[1]].add(a[2])
            
        allowed = f
        return self.helper(bottom, allowed, d)
        
        
        
        
    def helper(self, bottom, allowed, memo):
        if bottom in memo:
            return memo[bottom]
        if len(bottom) == 1:
            return True
        
        possible = [[] for _ in range(len(bottom) - 1)]
        
        for i in range(len(bottom) - 1):
            a = bottom[i]
            b = bottom[i + 1]
            possible[i] = list(allowed[a][b])
        
        next_bottoms = possible[0]
        for i in possible[1:]:
            a = copy.copy(next_bottoms)
            foo = []
            for j in i:
                foo.extend(x + j for x in a)
                
            next_bottoms = foo
            
        for i in next_bottoms:
            if i not in memo:
                memo[i] = self.helper(i, allowed, memo)
            if memo[i]:
                return True
        
        return False
                
        
        
        
        
