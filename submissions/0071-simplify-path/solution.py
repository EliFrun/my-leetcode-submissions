class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        stack = []
        for a in l:
            if a == "/" or a == "":
                continue
            elif a == '..':
                stack and stack.pop()
                
            elif a == ".":
                continue
            else:
                stack.append(a)
        ret = ""
        
        for a in stack:
            ret += '/'
            ret += a

        return ret if ret else "/"
