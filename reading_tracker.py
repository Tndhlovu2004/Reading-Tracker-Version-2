import json

try: 
 with open("name.json", "r") as file:
    name = json.load(file)
except FileNotFoundError:
  name = input("Hi! What is your name? ")

  with open("name.json", "w") as file:
   json.dump(name, file)
   
print(f"Hi {name}! Welcome to your Reading Tracker!")


