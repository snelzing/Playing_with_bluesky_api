from atproto import Client
import configparser

filename = "secrets.txt"

def get_username(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config.get("credentials", "username", fallback=None)

def get_password(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config.get("credentials", "password", fallback=None)

username = get_username("secrets.txt")
password = get_password("secrets.txt")

client = Client()
client.login(username, password)

post = client.send_post('Hello world! I posted this via the Python SDK because bluesky is cool like that')