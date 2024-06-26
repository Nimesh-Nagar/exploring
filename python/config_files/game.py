from configparser import ConfigParser
import random

config = ConfigParser()
config.read("game_config.ini")

user = input("What is your username : ")

if user == "SUDO":
    password = input("Password : ")
    if password != "123456":
        print("Wrong Password !")
        exit(0)

try:
    config_data = config[user]

except:
    print("User Not Found !!")
    exit(0)


number = random.randint(1, 10 ** (int(config_data["numberdigits"])))
max_tries = int(config_data["numbertries"])
tries = 0


while True:

    guess = input("Guess : ")
    if guess == "cheat":
        if "cheats" in config_data.keys() and config_data["cheats"] == "on":
            print(f"You won ! The number was {number}")
            exit(0)

        else:
            print("You are not allowed to cheat")
            exit(0)

    else:
        guess = int(guess)

    tries += 1

    if guess == number:
        print(f"You won ! The number was {number}")
        print(f"It took you {tries} Tries !")

    else:
        if tries == max_tries:
            print(f"You lost after {tries} Tries !")
            print(f"The number was {number}")
            exit(0)

        else:
            if guess > number:
                print("Too High ")
            else:
                print("Too Low ")
