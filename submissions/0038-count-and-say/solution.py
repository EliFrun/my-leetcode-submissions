class Solution:
    def default():
        return 0
    
    def countAndSay(self, n: int) -> str:
        counter = 1
        seq = "1"
        while counter < n:
            current_count = 0
            current_char = seq[0]
            new_seq = ""
            for c in seq:
                if c == current_char:
                    current_count += 1
                else:
                    new_seq += f'{current_count}{current_char}'
                    current_char = c
                    current_count = 1
            
            new_seq += f'{current_count}{current_char}'       
            seq = new_seq
            counter += 1
            
            
        return seq
            
        
        
