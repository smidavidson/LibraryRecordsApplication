
class TextMenu:


    @staticmethod
    def getMenuUserInput(options):
        isInputValid = False

        while not isInputValid:
            menuSelection = input("Enter a selection: ")

            try:
                intMenu = TextMenu.selectionInRange(menuSelection, options)
                return intMenu
            except ValueError:
                print("Please enter a valid selection")



    @staticmethod
    def selectionInRange(menuSelection, options):
        menuSelection = int(menuSelection)

        if (menuSelection < len(options) and menuSelection >= 0):
            return menuSelection

        else:
            raise ValueError


    @staticmethod
    def printOptions(options):
        for i in options:
            print("{}. {}".format(i, options[i]))