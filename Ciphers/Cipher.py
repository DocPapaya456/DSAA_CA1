from abc import ABC, abstractmethod

class Cipher(ABC):
    """Abstract base class for Ciphers providing encryption and decryption interface."""

    @abstractmethod
    def encrypt(self, plaintext: str) -> str:
        """Encrypt plain text string."""
        pass

    @abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        """Decrypt cipher text string."""
        pass

    def encryptFile(self, input_path: str, output_path: str) -> None:
        """Encrypt file contents from input_path and save to output_path."""
        with open(input_path, 'r', encoding='utf-8') as infile:
            contents = infile.read()

        processed = self.encrypt(contents)

        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(processed)

    def decryptFile(self, input_path: str, output_path: str) -> None:
        """Decrypt file contents from input_path and save to output_path."""
        with open(input_path, 'r', encoding='utf-8') as infile:
            contents = infile.read()

        processed = self.decrypt(contents)

        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(processed)
