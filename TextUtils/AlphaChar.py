class AlphaChar:
    def __init__(self, character):
        if len(character) != 1:
            raise ValueError("AlphaChar: length of 'character' should be 1")
        
        self.character = character
    
    def __add__(self, otherChar):
        if otherChar == None:
            raise TypeError("'+' not supported between instances of 'AlphaChar' and 'NoneType'")
        result = chr(ord('A') + (ord(self.character.upper()) + ord(otherChar.character.upper()) - 2*ord('A')) % 26)
        return result.lower() if self.character.islower() else result
    
    def __sub__(self, otherChar):
        if otherChar == None:
            raise TypeError("'+' not supported between instances of 'AlphaChar' and 'NoneType'")
        result = chr(ord('A') + (ord(self.character.upper()) - ord(otherChar.character.upper())) % 26)
        return result.lower() if self.character.islower() else result
    
    def __str__(self):
        return str(self.character)