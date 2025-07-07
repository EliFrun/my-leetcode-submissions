class Solution:
    def generateTag(self, caption: str) -> str:
        return ("#" + ''.join([(x[0].upper() if i > 0 else x[0].lower()) + x[1:].lower() for i, x in enumerate([y for y in caption.split(' ') if y])]))[:100]
