from gameData import game_data, genre
from random import randrange


# greet function and calls upon correct functions once the user has entered the data needed
def greet(name = None):
    # checking if name is none, decided to do it this way to loop
    if name is None:
        name = input("What is your name? ")
    # asks user if they would like to search by genre or user provided list and checks if the input data is correct if not recall function with name
    choice = input("Hello, {0} welcome to the game recommandion center. If you would like to input some games you wish to play please enter 1"\
        ", if you would prefer to choose by genre please enter 2 \n".format(name))
    choices = ["1", "2"]
    if choice not in choices:
        print("Please input either 1 or 2")
        return greet(name)
    # checking choice for user provided list else search by genre   
    if choice == "1":
        return user_supplied()
    else:
        age = age_check()
        return by_genre(age)

 
# checker for seeing if user wishes to have age rating search    
def age_check(choice = None):
    # list to check answer against
    choices = ["y", "n"]
    # Getting user input and checking answers
    if choice is None:
        choice = input("Would you like to set an age range for the recommended games. (y/n) ")
        if choice.lower() not in choices:
            print("Please input either y or n")
            return age_check()
    # getting the age group to search for
    if choice == "1":
        age_range = input("What age range would you like to look at? ")
        if int(age_range) < 0:
            print("Please enter only positive numbers.")
            return age_check(choice)
        return age_range
    # Returning 99 so when function compares it will be higher than all ages in the data
    else:
        return "99"
  
  
# If user wants to input a list of games this function is called   
def user_supplied():
    # setting up a list to store user's games and a list containing y / n to compare against
    game_list = []
    answers = ["y", "n"]
    # asking user for the first game and appending to list
    game = input("You have chosen to input your own list, please enter your first game: ")
    game_list.append(game)
    
    while True:
        # asking the user if they would like to add another game, if answer is not in list variable print error and ask user to try again
        more_games = input("Do you want to add another one?(y/n)")
        if more_games.lower() not in answers:
            print("Please enter a valid answer.")
            continue
        # if they dont want to break out of loop else ask for another game and append to list
        if more_games.lower() == "n":
            break
        new_game = input("Please enter your next game you wish to add: ")
        game_list.append(new_game)
    # once user has submitted all games they wish to play print out the game at a random spot in the list
    print("The game to play is going to be... {0}".format(game_list[randrange(len(game_list))]))
    
    
# searches a string either by first char if current_length is 0 or will search the length that is provided
def search_letter(letter, current_length = 0):
    matched_genre = []
    if current_length == 0:
        for current in genre:
            if letter.lower() == current[0].lower():
                matched_genre.append(current)
    else:
        for current in genre:
            if letter[:current_length].lower() == current[:current_length].lower():
                matched_genre.append(current)
    if len(matched_genre) == 0:
        return False
    return matched_genre


# compares the string provided against the genre list imported from gameData
def search_word(letter):
    matched_genre = []
    for current in genre:
        if current.lower() == letter.lower():
            matched_genre.append(current)
    if len(matched_genre) == 0:
        return False
    return matched_genre


# if user wishes to search by genre this function is called.
def by_genre(age):
    # setting some variables up for the function
    count = 2
    error_count = 0
    # asking the user to enter either the word or letter of the genre they wish to play
    letter = input("You have chosen to search by genre, Please enter the first letter of the game genre you wish to play,"\
                   "or the genre you wish to play. ")
    # checking user input if length of one call search_letter function, else call word
    if len(letter) == 1:
        result = search_letter(letter)
    else:
        result_of_word = search_word(letter)
        # if the search_word function returns false the program will search by first letter, if that also comes back with nothing prints an error and exits
        if result_of_word == False:
            print("Sorry i could not find that genre, we will now search by the first letter.")
            result = search_letter(letter[0])
            if result == False:
                print("I'm sorry we could not find {0} in our database. Please try again later".format(letter))
                exit()
        # else sends genre to data search function
        else:
            return data_search(result_of_word)
    # printing results of the auto correct
    print("Here are the results of the search: {0} ".format(result))
    # start of the loop, asks user to input the next letter up till count is greater than 3 then it will promp the user to input full name of the genre
    while True:
        # user has 3 attempts before the program will exit, decided to do it this way just incase any errors pops up the program will end
        if error_count > 2:
            print("Exiting, too many attempts")
            exit()
        
        letters = input("Please enter the beginning of the genre: ")
        results = search_letter(letters, count)
        # checking results of letter search, if it returns false promps the user to try again and increases error count
        if results == False:
            print("Please try again.")
            results = result
            error_count += 1
            continue
        # if only one genre comes back send genre to data search funciton
        elif len(results) == 1:
            return data_search(results)
        # printing results if more than one genre came back and increases count by 1 
        print("Here are the results of the search: {0} ".format(results))
        count += 1
        # checking if count is greater than 3 if so user will be prompted to input full name of the genre they wish to play
        if count > 3:
            # resetting errors back down to 0
            error_count = 0
            while True:
                
                word = input("Please enter the full genre name: ")
                results = search_word(word)
                # if result comes back false, check if error count is at limit if so exit else print error and try again
                if results == False:
                    if error_count > 2:
                        print("Exiting, too many attempts")
                        exit()
                    else:
                        print("Please try again")
                        error_count += 1
                        continue
                # else send data to data_search
                else:
                    return data_search(word)
                
            
        
def data_search(word):
    pass
       
                


print(greet())