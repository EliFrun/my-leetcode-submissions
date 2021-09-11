class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        if len(palindrome) % 2 == 0:
            for i, v in enumerate(palindrome):
                if v == 'a':
                    continue
                break

            if i == len(palindrome) - 1:
                return palindrome[:i] + "b"
            return palindrome[:i] + 'a' + palindrome[i + 1:]
        else:
            for i, v in enumerate(palindrome):
                if v == 'a':
                    continue
                break
            if i == len(palindrome) // 2:
                return palindrome[:-1] + "b"
            
            return palindrome[:i] + 'a' + palindrome[i + 1:]
            
        
