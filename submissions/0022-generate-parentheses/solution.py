class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = ['('] * n
        right = [')'] * n
        return list(set(self.helper(left, right)))
            
            
            
    def helper(self, left, right):
        print(left, right)
        if not right:
            return ['']
        if not left:
            return [''.join(right)]
        
        ret = []
        
        for i in range(1, len(left) + 1):
            ret.extend(
                [ "(" * i + x for x in self.helper(left[i:], right) ]
            )
        if len(right) > len(left):
            for i in range(1, len(right) - len(left) + 1):
                ret.extend(
                    [ ")" * i + x for x in self.helper(left, right[i:])  ]
                ) 

        return ret
