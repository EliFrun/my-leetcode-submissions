class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children

        ret = 0
        while money > 0 and ret < children:
            if money >= 7:
                ret += 1
                money -= 7
            else:
                break


        if money > 0:
            rem = children - ret
            return ret - 1 if rem == 0 or (rem == 1 and money == 3) else ret
        return ret

            


        
