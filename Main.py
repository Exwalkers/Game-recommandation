


def greet(name = None):
    if name is None:
        name = input("What is your name? ")
    choice = input("Hello, {0} welcome to the game recommandion center. If you would like to input some games you wish to play please enter 1"\
        ", if you would prefer to choose by genre please enter 2 \n".format(name))
    choices = ["1", "2"]
    if choice not in choices:
        print("Please input either 1 or 2")
        return greet(name)
        
    if choice == "1":
        print("Made it the input was : {0}".format(choice))
        return ## Add function here later
    elif choice == "2":
        print("Made it the input was : {0}".format(choice))
        return ## Add funciton here later
    
    
    
greet()