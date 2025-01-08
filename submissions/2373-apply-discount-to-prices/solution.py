class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        money_string = '0123456789'
        for i in range(len(words)):
            word = words[i]
            if word[0] == "$" and len(word) > 1 and all([x in money_string for x in word[1:]]):
                print(word)
                words[i] = f'${float(word[1:]) * (100 - discount)/100:.2f}'

        return " ".join(words)

        
