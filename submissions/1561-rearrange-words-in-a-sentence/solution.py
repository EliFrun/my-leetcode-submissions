class Solution:
    def arrangeWords(self, text: str) -> str:
        return ' '.join(word for idx, word in 
            sorted(
                enumerate(text.split(' ')),
                key=lambda x: (len(x[1]), x[0])
            )
        ).lower().capitalize()
        
