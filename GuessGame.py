import random


def get_guess_from_user():
    user_number = input("Please enter a guess between 1 and the difficulty you chose")
    print("Your guess is:", user_number)
    return int(user_number)


def generate_number(guessdifficulty):
    secret_number = random.randint(1, guessdifficulty)
    print("The number the machine chose was:", secret_number)
    return secret_number


def compare_results(user_number, secret_number):
    if user_number == secret_number:
        return True
    else:
        return False


def play(livedifficulty):
    score = compare_results(get_guess_from_user(), generate_number(livedifficulty))
    if score:
        print("Congratulations, you won")
        return True
    else:
        print("You lost, better luck next time")
        return False
