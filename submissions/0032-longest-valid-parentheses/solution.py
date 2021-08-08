class Solution:
    def longestValidParentheses(self, s: str) -> int:
        current_max = 0
        running_max = 0
        left_stack = []
        for p in s:
            if not left_stack:
                current_max = max(current_max, running_max)
            if p == '(':
                left_stack.append(p)
            
            if p == ')':
                if left_stack:
                    left_stack.pop()
                    running_max += 2
                else:
                    left_stack = []
                    current_max = max(current_max, running_max)
                    running_max = 0
                    
        current_max = max(current_max, running_max) if not left_stack else current_max
                    
        r_current_max = 0
        r_running_max = 0
        right_stack = []
        for p in reversed(s):
            if not right_stack:
                r_current_max = max(r_current_max, r_running_max)
            if p == ')':
                right_stack.append(p)
            
            if p == '(':
                if right_stack:
                    right_stack.pop()
                    r_running_max += 2
                else:
                    right_stack = []
                    r_current_max = max(r_current_max, r_running_max)
                    r_running_max = 0
        r_current_max = max(r_current_max, r_running_max) if not right_stack else r_current_max
        
        return max(current_max, r_current_max)
