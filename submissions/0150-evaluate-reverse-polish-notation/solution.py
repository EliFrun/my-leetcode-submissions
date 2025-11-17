class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        mp = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: b - a,
            "*": lambda a,b: a * b,
            "/": lambda a,b: int(b / a),
        }
        for token in tokens:
            if token in "*/+-":
                stk.append(mp[token](stk.pop(), stk.pop()))
            else:
                stk.append(int(token))
        return int(stk[0])
                
        
