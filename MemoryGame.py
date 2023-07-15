import random
from time import sleep
from Utils import Screen_cleaner


def generate_sequence(memorydifficulty):
    randomlist = random.sample(range(1, 101), memorydifficulty)
    print("randomlist is :", randomlist)
    sleep(0.8)
    Screen_cleaner()
    return randomlist


def get_list_from_user(difficulty):
    userlist = list(map(int, input("Enter the numbers you remember separated by spaces : ").strip().split()))[
               :difficulty]
    return userlist


def is_list_equal(randomlist, userlist):
    if userlist == randomlist:
        return True
    else:
        return False


def play(livedifficulty):
    score = is_list_equal(generate_sequence(livedifficulty), get_list_from_user(livedifficulty))
    if score:
        print("Congratulations, you win!")
        return True
    else:
        print("You lost, better luck next time")
    return False
