class Solution:
    def originalDigits(self, s: str) -> str:
            # zero
            # one
            # two
            # three
            # four
            # five
            # six
            # seven
            # eight
        # nine
        
        counts = defaultdict(int)
        for ch in s:
            counts[ch] += 1
           
        ret = defaultdict(int)
        # check for zeroes
        if counts['z'] > 0:
            ret['0'] = counts['z']
            counts['e'] -= counts['z']
            counts['o'] -= counts['z']
            counts['r'] -= counts['z']
            counts['z'] = 0
            
        # check twos
        if counts['w'] > 0:
            ret['2'] = counts['w']
            counts['t'] -= counts['w']
            counts['o'] -= counts['w']
            counts['w'] = 0
        
        # check six
        if counts['x'] > 0:
            ret['6'] = counts['x']
            counts['s'] -= counts['x']
            counts['i'] -= counts['x']
            counts['x'] = 0
            
        # check sevens
        if counts['s'] > 0:
            ret['7'] = counts['s']
            counts['v'] -= counts['s']
            counts['e'] -= 2 * counts['s']
            counts['n'] -= counts['s']            
            counts['s'] = 0
            
        # check fives
        if counts['v'] > 0:
            ret['5'] = counts['v']
            counts['f'] -= counts['v']
            counts['i'] -= counts['v']
            counts['e'] -= counts['v']            
            counts['v'] = 0
            
        # check fours
        if counts['f'] > 0:
            ret['4'] = counts['f']
            counts['o'] -= counts['f']
            counts['u'] -= counts['f']
            counts['r'] -= counts['f']            
            counts['f'] = 0
            
        # check ones
        if counts['o'] > 0:
            ret['1'] = counts['o']
            counts['n'] -= counts['o']
            counts['e'] -= counts['o']            
            counts['o'] = 0
            
        # check threes
        if counts['r'] > 0:
            ret['3'] = counts['r']
            counts['t'] -= counts['r']
            counts['h'] -= counts['r']
            counts['e'] -= 2 * counts['r']            
            counts['r'] = 0
            
        # check eights
        if counts['h'] > 0:
            ret['8'] = counts['h']
            counts['e'] -= counts['h']
            counts['i'] -= counts['h']
            counts['g'] -= counts['h'] 
            counts['t'] -= counts['h'] 
            counts['h'] = 0
            
        # check nines
        if counts['i'] > 0:
            ret['9'] = counts['i']
            counts['n'] -= 2 * counts['i']
            counts['e'] -= counts['i']            
            counts['i'] = 0
            
        ans = ""
        
        
        for ch in "0123456789":
            ans += ch * ret[ch]
            
        return ans
            
    
        
