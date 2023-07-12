import random
import requests
import json
import math


def get_money_interval():
    usdamount = random.randint(1, 100)
    currencyapi = requests.get(
        "https://api.freecurrencyapi.com/v1/latest?apikey=6DfmleX0dZoJMEq95hGXjwQOHosivhxRDGhWcvFk&currencies=ILS")
    if currencyapi.status_code == 200:
        data = currencyapi.json()
    else:
        print("request failed, error code:", currencyapi.status_code)
    usdtoils = data['data']['ILS']
    totalvalue = usdamount * float(usdtoils)
    print('generated usdamount', usdamount)
    return totalvalue


def get_guess_from_user():
    userguess = input("Please enter your guess")
    print("Your guess is:", userguess)
    return float(userguess)


def play(difficulty):
    totalvalue = get_money_interval()
    negativeinterval = totalvalue-5-difficulty
    positiveinterval = totalvalue+5-difficulty
    userguess = get_guess_from_user()
    if math.isclose(negativeinterval, userguess) or math.isclose(positiveinterval, userguess) or (negativeinterval <= userguess <= positiveinterval):
        print("Congratulations, you won")
        return True
    else:
        print("You lost, better luck next time")
        return False


