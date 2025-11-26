class TextUtils:
    @staticmethod
    def seperateLettersPunctuation(text):
        letters = ""
        punctuation = ""
        i = 0
        for char in text:
            if char.isalpha():
                letters += char
                i += 1
            else:
                punctuation += str(i) if i > 0 else ""
                punctuation += char
                i = 0
        return letters, punctuation
    
    @staticmethod
    def combineLettersPunctuation(letters, punctuation):
        text = ""

        start = 0
        end = 0
        for c in punctuation:
            if c.isdigit():
                end += int(c)
                text += letters[start:end]
                start = end
                continue
            text += c
        return text