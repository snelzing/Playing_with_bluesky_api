import configparser

filename = "secrets.txt"

def get_password(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config.get("credentials", "password", fallback=None)

password = get_password("secrets.txt")
print("Password:", password)
