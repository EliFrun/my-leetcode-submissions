class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)

        for i in range(len(num)):
            if change[int(num[i])] > int(num[i]):
                j = i
                while j < len(num) and change[int(num[j])] >= int(num[j]):  
                    num[j] = str(change[int(num[j])])
                    j += 1
                break
        return ''.join(num)
        
