import json

try: 
 with open("name.json", "r") as file:
    name = json.load(file)
except FileNotFoundError:
  name = input("Hi! What is your name? ")

  with open("name.json", "w") as file:
   json.dump(name, file)
 
try: 
 with open("year.json", "r") as file:
  year = json.load(file)
except FileNotFoundError:

  while True:
   try:
    year = int(input("What is your current reading year? "))
    break
   except ValueError:
     print("The year has to be a whole number. Please try again.")

  with open("year.json", "w") as file:
   json.dump(year, file)

print(f"Hi {name}! Welcome to your Reading Tracker!")
print()

try:
  with open("books.json", "r") as file:
   books = json.load(file)
except FileNotFoundError:
   books = []
   
def add_book():

  title = input("What is the title of your book? ")
  author = input("Who wrote this book? ")
  genre = input("What genre does this book belong to? ")

  while True:
   try: 
    rating = int(input("What would you rate this book /5? "))
    if rating < 1 or rating > 5:
     print("Rating has to be between 1 and 5. Please try again.")
     continue
    break
   except ValueError:
    print("The rating should be a whole number. Please try again.")
    
  book = {"Title": title,
        "Author": author,
        "Rating": rating,
        "Genre": genre}
  
  print()
  print("You have added the book: ")
  print(f"Title: {book["Title"]}")
  print(f"Author: {book["Author"]}")
  print(f"Rating: {book["Rating"]}")
  print(f"Genre: {book["Genre"]}")
  print()

  books.append(book)

  with open("books.json", "w") as file:
   json.dump(books, file)

  input("Press enter to return to menu.")

def view_books():

   if len(books) == 0:
     print("You have not added any books yet.")
   else: 
    print(f"In {year}, you have read the following books: ")
    print()
    for book in books:
      print(f"Title: {book["Title"]}")
      print(f"Author: {book["Author"]}")
      print(f"Rating: {book["Rating"]}")
      print(f"Genre: {book["Genre"]}")
      print()

   input("Press enter to return to menu.")
  
while True:

 print("----------------------------------------------")
 print("************** READING TRACKER ***************")
 print("----------------------------------------------")

 print("1. Add a book.")
 print("2. View your books.")
 print("3. Exit.")
 print()

 while True:
   try:
    option = int(input("What would you like to do? "))
    print()
    if option < 1 or option > 3:
      print("Your option has to be between 1 and 3. Please try again.")
      continue
    break
   except ValueError:
    print("Option is not valid. Please try again.")

 if option == 1: 
   add_book()
 if option == 2:
   view_books()
 if option == 3:
   break
   
   

   



