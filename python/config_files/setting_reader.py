from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())

try:
    config.read("settings.ini")
except Exception as error:
    print(f"[Error ] : {error}")
    raise SystemExit()

# like dictionary we can access values from .ini file
print(config["Log"]["log_filename"])  # here [Log] is section and [log_filename] is key
print(config["Database"]["server"])

# we can check key is present or not
if "username" in config["Database"]:
    print("username Exists")

print(config.get("Database", "password"))

print(config.sections())  # all sections in list
print(config.options("Database"))  # all keys in section

# print(type(config["Database"]["port"]))
# port = int(config["Database"]["port"])
# print(port , type(port))

port = config.getint("Database", "port")
print(port, type(port))

if config.getboolean("Log", "logging_on"):
    print("Logging On.....")
else:
    print("Logging off")

print(config["Log"]["log_dir"])
# print(config["Database"]["archive_dir"])
