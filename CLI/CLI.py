from CLI.Menu import Menu

class CLI:
    """Handles command-line user interface logic."""

    def __init__(self) -> None:
        self.menu = Menu()
    
    def run(self) -> None:
        """Main application loop."""
        self.menu.displayWelcome()
        while True:
            try:
                self.menu.displayOptions()
                option = input("Enter choice: ")
                if option == '7':
                    print('\nBye, thanks for using ST1507 DSAA: Keyword Cipher Encrypted Message Analyzer')
                    break

                # Validate option range
                if not (option.isdigit() and 0 < int(option) < 7):
                    print(f'Option "{option}" does not exist. Please try again.')
                    continue
                
                print()
                self.menu.runOption(option)
            except KeyboardInterrupt:
                print('Keyboard Interrupt detected. Returning to main menu...')
                input('Press Enter, to continue...')
