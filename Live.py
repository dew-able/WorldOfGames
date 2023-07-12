from GuessGame import play as guess_play
from CurrencyRouletteGame import play as currency_play
from MemoryGame import play as memory_play
from Score import add_score


def welcome(username):
    print(f"Hello {username} and welcome to the World of Games (WoG).\nHere you can find many cool games to play!")


def load_game():
    choice = int(input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 "
                       "second and you have to guess it back \n2. Guess Game - guess a number and see if you chose "
                       "like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD "
                       "in ILS"))
    while choice not in [1, 2, 3]:
        choice = int(input("Please choose a valid option:\n1. Memory Game - a sequence of numbers will appear for 1 "
                           "second and you have to guess it back \n2. Guess Game - guess a number and see if you chose "
                           "like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD"
                           "in ILS"))

    difficulty = int(input("Please choose game difficulty from 1 to 5"))
    while difficulty not in [1, 2, 3, 4, 5]:
        print("Please choose a valid option")
        difficulty = int(input("Please choose game difficulty from 1 to 5"))
    if choice == 1:
        result = memory_play(difficulty)
    if choice == 2:
        result = guess_play(difficulty)
    if choice == 3:
        result = currency_play(difficulty)

    if result:
        print(result)
        add_score(difficulty)
    return difficulty


load_game()
