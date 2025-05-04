class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ret = []
        for i in range(len(target)):
            c = target[i]
            for j in range(ord(c) - ord('a') + 1):
                ret.append(target[:i] + chr(ord('a') + j))
        return ret

        
