from gameData import game_data, genres
from random import randrange
from Linkedlist import LinkedList

choices = ["y", "n"]

# function for setting up a linked list for all game genre's
def genre_data():
    genre_data = LinkedList()
    for genre in genres:
        genre_data.insert_data(genre)
    return genre_data


# function for setting up a linkedlist with all games inside
def games():
    all_games = LinkedList()
    for genre in genres:
        sub_genre_list = LinkedList()
        for game in game_data:
            if game[0] == genre:
                sub_genre_list.insert_data(game)
        all_games.insert_data(sub_genre_list)
    return all_games


# function for placing all genre's into a list to use to compare against
def list_genres():
    game_genres = genre_data() 
    genres_head = game_genres.get_head_node()
    genre_list = []
    while genres_head.get_next_node() is not None:
        genre_list.append(genres_head.get_value())
        genres_head = genres_head.get_next_node()
    return genre_list


# greet function and calls upon correct functions once the user has entered the data needed
def greet(name = None):
    # checking if name is none, decided to do it this way to loop
    if name is None:
        name = input("What is your name? \n")
    # asks user if they would like to search by genre or user provided list and checks if the input data is correct if not recall function with name
    lines()
    answer = input("Hello, {0} welcome to the game recommandion center. If you would like to input some games you wish to play please enter 1"\
        ", if you would prefer to choose by genre please enter 2 \n".format(name))
    choice = ["1", "2"]
    
    if answer not in choice:
        print("Please input either 1 or 2")
        return greet(name)
    # checking choice for user provided list else search by genre   
    if answer == "1":
        return user_supplied()
    else:
        age = age_check()
        return by_genre(age)

 
# checker for seeing if user wishes to have age rating search    
def age_check(choice = None):
    # list to check answer against
    # Getting user input and checking answers
    if choice is None:
        lines()
        choice = input("Would you like to set an age range for the recommended games. (y/n) \n")
        if choice.lower() not in choices:
            print("Please input either y or n")
            return age_check()
    # getting the age group to search for
    if choice == "y":
        lines()
        age_range = input("What age range would you like to look at? \n")
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
    # asking user for the first game and appending to list
    lines()
    game = input("You have chosen to input your own list, please enter your first game: \n")
    game_list.append(game)
    
    while True:
        # asking the user if they would like to add another game, if answer is not in list variable print error and ask user to try again
        lines()
        more_games = input("Do you want to add another one?(y/n) \n")
        if more_games.lower() not in choices:
            print("Please enter a valid answer.")
            continue
        # if they dont want to break out of loop else ask for another game and append to list
        if more_games.lower() == "n":
            break
        lines()
        new_game = input("Please enter your next game you wish to add: \n")
        game_list.append(new_game)
    # once user has submitted all games they wish to play print out the game at a random spot in the list
    print("The game to play is going to be... {0}".format(game_list[randrange(len(game_list))]))
    
    
# function for compairing the user's input data versus the genre's in the linkedlist(using list_genres function above)
def search_letter(letter):
    matched_genre = []
    genre = list_genres()
    for gen in genre:
        if gen[:len(letter)].lower() == letter.lower():
            matched_genre.append(gen)
    if not matched_genre:
        return None
    return matched_genre

# function for printing lines to break up text between questions
def lines():
    return print("-" * 180)


# if user wishes to search by genre this function is called.
def by_genre(age):
    print("Here is the list of all genre's in the database: {0}".format(list_genres()))
    lines()
    user_letter = input("You have chosen to search by genre, Please enter the first letter of the game genre you wish to play,"\
                   "or the genre you wish to play. \n")
    result = search_letter(user_letter)
    if result is None:
        lines()
        print("There were no results found of the search of: {0}. Please try again.".format(user_letter))
        lines()
        return by_genre(age)
    while True:
        if result is None:
            lines()
            print("Could not find any results on your search of: {0}".format(user_letter))
            result = search_letter(user_letter[0])
        if len(result) == 1:
            break
        else:
            lines()
            temp_user_letter = input("Here is the results of the search, please input the next letter of full word: {0} \n".format(result))
            if len(temp_user_letter) == 1:
                user_letter = user_letter + temp_user_letter
                result = search_letter(user_letter)
            else:
                user_letter = temp_user_letter
                result = search_letter(user_letter)
    data_search(result, age)
            
    
                
            
# final function for looking through the data for games that match the user's genre they wish to see        
def data_search(word, age):
    matched_games = []
    # calles the games function and sets up a variable to be the head node to start a while loop with
    games_list = games()
    head = games_list.get_head_node()
    # while loop to compare requests genre versus the data in the games linkedlist
    while head.get_next_node() is not None:
        sub_head = head.get_value().get_head_node()
        if sub_head.get_value()[0].lower() == word[0].lower():
            while sub_head.get_next_node() is not None:
                if int(sub_head.get_value()[2]) < int(age):
                    matched_games.append(sub_head.get_value()[1])
                sub_head = sub_head.get_next_node()
        head = head.get_next_node()
        
    # If not games are compatiable with the age rating print error
    if not matched_games:
        print("there were no games found that match your criteria, please try again with a different age rating ")
    # This if statement is here due to current data set where there is a chance to only get one game returned
    elif len(matched_games) == 1:
        print("The game to play from the {0} genre is: {1}".format(word[0], matched_games[0]))
    # else ask the user if they would like to see all games in the genre or if no print a random game for them to play 
    else:
        lines()
        answer = input("Would you like all games printed out from the list from the genre {0}: (y/n) \n".format(word[0]))
        if answer.lower() not in choices:
            print("Please try again.")
            return data_search(word, age)
        elif answer.lower() == "y":
            lines()
            print("Here are the games that match your genre of {0}: ".format(word[0]))
            for item in matched_games:
                print(item)
        else:
            print("Here is the game we recommend you to play!: {0}".format(matched_games[randrange(len(matched_games))][0]))
        
                
        
    

greet() 
