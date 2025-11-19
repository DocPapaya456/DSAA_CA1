from CLI.Menu import Menu
def main():
    menu = Menu()
    menu.displayWelcome()
    while True:
        menu.displayOptions()
        option = input("Enter choice: ")
        if option == '7':
            print('\nBye, thanks for using ST1507 DSAA: Keyword Cipher Encrypted Message Analyzer')
            break

        if not (option.isdigit() and int(option) > 0 and int(option) < 7):
            print(f'Option "{option}" does not exist. Please try again.')
            continue
        
        print()
        menu.runOption(option)
        

            

    
if __name__ == "__main__":
    main()