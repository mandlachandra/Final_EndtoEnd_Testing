import configparser

config = configparser.ConfigParser()
config.read("config.ini")

base_url = config["default"]["base_url"]
browser = config["defaulr"]["browser"]
timeout = config["default"]['browser']

print(f"url: {base_url}")
print(f"browser: {browser}")
print(f"timeout: {timeout}")