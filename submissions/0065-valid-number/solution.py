class Solution:
    def isNumber(self, s: str) -> bool:
        decimal_sign = ""
        decimal = ""
        decimal_point = ""
        decimal_2 = ""
        
        exponent_exists = False
        
        exponent_sign = ""
        exponent = ""
        
        
        if s and (s[0] == "-" or s[0] == "+"):
            decimal_sign = s[0]
            s = s[1:]
            
        if s and s[0].isnumeric():
            i = 0
            while i < len(s) and s[i].isnumeric():
                decimal += s[i]
                i += 1               
            s = s[i:]
                
        if s and s[0] == ".":
            decimal_point += s[0]
            s = s[1:]
            
        if s and s[0].isnumeric():
            i = 0
            while i < len(s) and s[i].isnumeric():
                decimal_2 += s[i]
                i += 1
                
            s = s[i:]            
                
        if s and s[0].lower() == "e":
            s = s[1:]
            exponent_exists = True
            
        if exponent_exists:
            if s and (s[0] == "-" or s[0] == "+"):
                exponent_sign = s[0]
                s = s[1:]


            if s and s[0].isnumeric():
                i = 0
                while i < len(s) and s[i].isnumeric():
                    exponent += s[i]
                    i += 1     
                s = s[i:]


        
        print(
            decimal_sign,
            decimal,
            decimal_point,
            decimal_2,
            exponent_exists,
            exponent_sign,
            exponent
        )
        if s:
            return False
                
        else:
            return (
                ((not decimal_sign) or (decimal or (decimal_point and decimal_2))) and
                ((not decimal_point) or (decimal or decimal_2)) and
                ((not exponent_exists) or (decimal or decimal_2)) and
                ((not exponent_exists) or exponent) and 
                ((not exponent_sign) or exponent)
            )
