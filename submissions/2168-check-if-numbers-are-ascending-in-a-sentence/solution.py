class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = [int(x) for x in re.sub('[a-zA-Z]', ' ', s).split(' ') if x.isnumeric()]
        for i in range(len(s) - 1):
            if s[i] >= s[i + 1]:
                return False
        return True

        
        
