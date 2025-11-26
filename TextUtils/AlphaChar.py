class AlphaChar:
    """Represents a single alphabetic character for cipher arithmetic operations."""

    def __init__(self, character: str) -> None:
        if len(character) != 1:
            raise ValueError("AlphaChar: length of 'character' should be 1")
        self.character = character
    
    def __add__(self, otherChar: "AlphaChar") -> str:
        """Implements letter shift addition (A+1=B type logic)."""
        if otherChar is None:
            raise TypeError("'+' not supported between instances of 'AlphaChar' and 'NoneType'")
        result = chr(ord('A') + (ord(self.character.upper()) + ord(otherChar.character.upper()) - 2 * ord('A')) % 26)
        return result.lower() if self.character.islower() else result
    
    def __sub__(self, otherChar: "AlphaChar") -> str:
        """Implements letter shift subtraction (C-A=B type logic)."""
        if otherChar is None:
            raise TypeError("'-' not supported between instances of 'AlphaChar' and 'NoneType'")
        result = chr(ord('A') + (ord(self.character.upper()) - ord(otherChar.character.upper())) % 26)
        return result.lower() if self.character.islower() else result
    
    def __str__(self) -> str:
        return str(self.character)
