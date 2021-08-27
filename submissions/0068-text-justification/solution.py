class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rows = []
        
        current_row = []
        current_len = 0
        for word in words:
            if current_row:
                if (current_len + len(word) + 1) > maxWidth:
                    rows.append(current_row)
                    current_row = [word]
                    current_len = len(word)
                else:
                    current_row.append(word)
                    current_len += len(word) + 1
            else:
                current_row.append(word)
                current_len = len(word)
                
        rows.append(current_row)
                
        
        ret = []
        for r in enumerate(rows):
            row = r[1]
            if r[0] == len(rows) - 1:
                line = ""
                l = 0
                for w in enumerate(row):
                    word = w[1]
                    if w[0] == len(row) - 1:
                        line += word
                        line += " " * (maxWidth - l - len(word))
                    else:
                        line += f'{word} '
                        l += len(word) + 1
                        
                ret.append(line)
            else:
                number_of_spaces = maxWidth - sum(len(x) for x in row)
                spaces_per_word = number_of_spaces // max(1, len(row) - 1)
                extra_spaces = number_of_spaces % max(1, len(row) - 1)
                i = 1
                lis = []
                for word in row:
                    lis.append(word)
                    if i < len(row) or len(row) == 1:
                        if extra_spaces > 0:
                            lis.append(" " * (spaces_per_word + 1))
                            extra_spaces -= 1
                        else:
                            lis.append(" " * spaces_per_word)

                    i += 1
                line = ""
                for l in lis:
                    line += l

                ret.append(line)
            
        return ret
