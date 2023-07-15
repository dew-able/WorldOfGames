import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = int(000)


def Screen_cleaner():
    try:
        os.system('clear')
    finally:
        print("\n"*20)
    try:
        os.system('cls')
    finally:
        print("\n"*20)


