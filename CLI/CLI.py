from CLI.Menu import Menu
class CLI:
    def __init__(self):
        self.menu = Menu()
    
    def run(self):
        self.menu.displayWelcome()
        while True:
            self.menu.displayOptions()
            option = input("Enter choice: ")
            if option == '7':
                print('\nBye, thanks for using ST1507 DSAA: Keyword Cipher Encrypted Message Analyzer')
                break

            if not (option.isdigit() and int(option) > 0 and int(option) < 7):
                print(f'Option "{option}" does not exist. Please try again.')
                continue
            
            print()
            self.menu.runOption(option)