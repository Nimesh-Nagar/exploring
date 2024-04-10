from configparser import ConfigParser

config = ConfigParser()

config["Default"] = {
    "numberdigits": 6, 
    "numbertries": 8, 
    "playername": "Player"
    }

config["NeuralNine"] = {
    "numberdigits": 10, 
    "numbertries": 5, 
    "playername": "Nimesh"
    }

config["SUDO"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername": "Cheater",
    "cheats": "on",
}

with open("game_config.ini", "w") as f:
    config.write(f)


