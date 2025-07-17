import configparser

#create config object and read file
config = configparser.ConfigParser()
config.read("config.ini")

#read values
base_url = config["Default"]["base_url"]
browser = config["Default"]["browser"]
timeout = int(config["Default"]["timeout"])

username = config["credentials"]["username"]
password = config["credential"]["password"]

print(f"URL:{base_url}")
print(f"Browser: {browser}")
print(f"timeout: {timeout}")
print(f"userame:{username}, password:{password}")
