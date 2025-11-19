
from CLI.Options import Options

class Menu(Options):
    def __init__(self):
        super().__init__()

    
    # Display Welcome Screen
    def displayWelcome(self):
        print('''
    *********************************************************
    *                                                       *
    *     ~ Keyword Cipher Encrypted Message Analyzer ~     *
    *-------------------------------------------------------*
    *                                                       *
    *  - Done by: Nathan Soon (2401421)                     *
    *  - Class DAAA/2A/21                                   *
    *********************************************************
            ''')
        input("Press Enter, to continue...")
        print()

    # Display menu options
    def displayOptions(self):
        print(
            '''
    Please select your choice: (1,2,3,4,5,6,7)
    \t1. Encrypt/Decrypt File
    \t2. Letter frequency distribution
    \t3. Infer cipher keyword
    \t4. Batch Decryption
    \t5. Extra Option One
    \t6. Extra Option Two
    \t7. Exit
            '''
        )

    