from CLI.Options import Options

class Menu(Options):
    """Menu class responsible for displaying user options."""

    def __init__(self) -> None:
        super().__init__()

    def displayWelcome(self) -> None:
        """Displays welcome screen."""
        print('''
*********************************************************
* ST1507 DSAA: Welcome to:                              *
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

    def displayOptions(self) -> None:
        """Displays options for main menu."""
        print(
            '''
Please select your choice: (1,2,3,4,5,6,7)
\t1. Encrypt/Decrypt File
\t2. Letter frequency distribution
\t3. Infer cipher keyword
\t4. Batch Decryption
\t5. Encrypt/Decrypt File using Vigenère
\t6. Infer Vigenère key length
\t7. Exit
            '''
        )
