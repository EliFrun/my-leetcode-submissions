class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def counter_compare(ref, curr):
            return all([curr[k] >= v for k,v in ref.items()])
        t_counter = Counter(t)
        curr_window = defaultdict(int)

        left, right = 0,0
        ret_left, ret_right = -1, -1
        while right < len(s):
            if left == right:
                curr_window[s[right]] += 1
                right += 1

            good = counter_compare(t_counter, curr_window)
            if good:
                if ret_left == -1:
                    ret_left = left
                    ret_right = right
                elif ret_right - ret_left > right - left:
                    ret_left = left
                    ret_right = right
                
                curr_window[s[left]] -= 1
                if curr_window[s[left]] <= 0:
                    curr_window.pop(s[left])
                left += 1
            
            elif right < len(s):
                curr_window[s[right]] += 1
                right += 1

        while left < len(s) and counter_compare(t_counter, curr_window):
            if ret_left == -1:
                ret_left = left
                ret_right = right
            if right - left < ret_right - ret_left:
                ret_right = right
                ret_left = left

            curr_window[s[left]] -= 1
            if curr_window[s[left]] <= 0:
                curr_window.pop(s[left])
            left += 1

        return s[ret_left: ret_right]
            
        
        
