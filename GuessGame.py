import random


def generate_number(guessdifficulty):
    secret_number = random.randint(1, guessdifficulty)
    return secret_number


def get_guess_from_user():
    user_number = input("Please enter your guess")
    print("Your guess is:", user_number)
    return int(user_number)


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
