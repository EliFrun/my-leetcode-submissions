class Solution:
    def myAtoi(self, s: str) -> int:
        ret = ""
        neg = False
        a_num = False
        for i in s:
            if i <= '9' and i>= '0':
                neg = True
                a_num = True
                ret += i
                
            elif i == ' ':
                if a_num:
                    break
                else:
                    next
            elif i == '+':
                if a_num:
                    break
                else:
                    a_num = True
            elif i == '-':
                if not neg and not a_num:
                    neg = True
                    a_num = True
                    ret += i
                else:
                    if a_num:
                        break
                    if neg:
                        return 0
            elif not a_num:
                return 0
            else:
                break
        try:   
            val = int(ret)
            if abs(int(ret)) < 2**31:
                pass
            else:
                val = int(2**31 * (int(ret)/ abs(int(ret))))
                if val > 0:
                    val -= 1
            return val
        except:
            return 0
