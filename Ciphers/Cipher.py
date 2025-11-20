from abc import ABC, abstractmethod

class Cipher(ABC):

    @abstractmethod
    def encrypt(self, plaintext):
        pass

    @abstractmethod
    def decrypt(self, ciphertext):
        pass

    # Encrypts file contents from input_path and outputs into output_path
    def encryptFile(self, input_path, output_path):

        # Read from input file
        with open(input_path, 'r', encoding='utf-8') as infile:
            contents = infile.read()

        # Encrypt file contents
        processed = self.encrypt(contents)

        # Write processed data to output file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(processed)

    # Decrypts file contents from input_path and outputs into output_path
    def decryptFile(self, input_path, output_path):
        # Read from input file
        with open(input_path, 'r', encoding='utf-8') as infile:
            contents = infile.read()

        # Encrypt file contents
        processed = self.decrypt(contents)

        # Write processed data to output file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(processed)