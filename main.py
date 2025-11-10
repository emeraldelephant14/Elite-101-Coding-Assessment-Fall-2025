from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author


def print_available():
    for book in library_books:
        if book["available"] == True:
            print(f"ID: {book["id"]}")
            print(f"Title: {book["title"]}")
            print(f"Author: {book["author"]}")
            print()
    print()


        
print_available()

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search_book():
    #empty list so we can add the book to the return list if the genre/author matches up with the term
    returned_books = []
    term = input("Enter a search term: ")

    #checking each book's genre and author
    for book in library_books:
        if book["author"].lower() == term.lower(): #checking if book's author matches up with the user-entered term
            returned_books.append(book["title"]) #adding it to a list so we can return more than one item
        if book["genre"].lower() == term.lower(): #checking if book's genre matches up with the user-entered term
            returned_books.append(book["title"]) 

    return returned_books

print(search_book())


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout():
    chosen_book = input("Which book would you like to check out? Please enter its ID: ")
    #If the book is B6, the book_number is 6. I am trying to access the index of the book in the list.
    book_number = int(chosen_book[1])
    #Python uses 0-indexing, so we have to subtract by 1 to access the correct book
    book_index = book_number-1

    if library_books[book_index]["available"] == False:
        print("This book is not available. Please check out another book.")
    else:
        library_books[book_index]["available"] = False
        library_books[book_index]["checkouts"] +=1

        #find the date and time right now
        now = datetime.now()

        #I used timedelta to find the exact time after 2 weeks (14 days)
        two_weeks = timedelta(days=+14)

        library_books[book_index]["due_date"]=str((now + two_weeks).date()) #now+two_weeks is two weeks from the current time
        #I used .date() for the code above to format the date in a year-month-day format
        #I also casted the date object to a string so it does not cause complications in the code later when I do comparisons between dates.
        print(f"Your book, {library_books[book_index]["title"]}, will be due on {library_books[book_index]["due_date"]}")
    print()

checkout()


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date


def return_book():
    returned_book = input("Which book would you like to return? Please use its ID: ")
    book_number = int(returned_book[1])
    #Python uses 0-indexing, so we have to subtract by 1 to access the correct book
    book_index = book_number-1

    library_books[book_index]["available"] = True
    library_books[book_index]["due_date"] = None
    print(f"The book {library_books[book_index]["title"]} has been successfully returned.")
    print()



return_book()

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def view_overdue():
    overdue_books = []
    for book in library_books:
        #Looking for books that are not available, meaning they are checked out
        if book["available"] == False:

            #This avoids having to compare a String with "None"            
            if book["due_date"] != None:
                
                #With the code below, I am checking if the due date passed by comparing the due_date to the date object, which is type string now.
                if book["due_date"] < str(datetime.now().date()):
                    overdue_books.append(book["title"])

    return(overdue_books)

print(f"The following books are overdue:{view_overdue()}")   



# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

class Book:
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def print_available(book_list):
        for book in book_list:
            if book.available == True:
                print(f"ID: {book.id}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
        print()

    def search(book_list):
    #empty list so we can add the book to the return list if the genre/author matches up with the term
        returned_books = []
        term = input("Enter a search term: ")

        #checking each book's genre and author
        for book in book_list:
            if book.author.lower() == term.lower(): #checking if book's author matches up with the user-entered term
                returned_books.append(book.title) #adding it to a list so we can return more than one item
            if book.genre.lower() == term.lower(): #checking if book's genre matches up with the user-entered term
                returned_books.append(book.title)
 

        return returned_books

    def checkout(book_list):
        chosen_book = input("Which book would you like to check out? Please enter its ID: ")
        for book in book_list:
            if book.id == chosen_book:
                if book.available == False:
                    print("This book is not available. Please check out another book.")

                else:
                    book.available = False
                    book.checkouts+=1

                    now=datetime.now()
                    two_weeks = timedelta(days=+14)
                    book.due_date = str((now+two_weeks).date())
                    print(f"Your book, {book.title}, will be due on {book.due_date}")
        print()

    def return_book(book_list):
        returned_book = input("Which book would you like to return? Please use its ID: ")

        for book in book_list:
            if book.id == returned_book:
                book.available = True
                book.due_date = None
                print(f"The book {book.title} has been successfully returned.")
                print()
                break
        else:
            print("This ID does not exist in the system.")


    def view_overdue(book_list):
        overdue_books = []
        for book in book_list:
            #Looking for books that are not available, meaning they are checked out
            if book.available == False:

                #This avoids having to compare a String with "None"            
                if book.due_date != None:
                    
                    #With the code below, I am checking if the due date passed by comparing the due_date to the date object, which is type string now.
                    if book.due_date < str(datetime.now().date()):
                        overdue_books.append(book.title)

        return(overdue_books)
    
    def view_popular(book_list):
        checkout_list = []
        for book in book_list:
            checkout_list.append(book.checkouts)
        checkout_list.sort(reverse = True)
        

  

    

        
if __name__ == "__main__":
    # You can use this space to test your functions

    #each book is an object of the Book class
    book1 = Book("B1", "The Lightning Thief", "Rick Riordan", "Fantasy", True, None, 2)
    book2 = Book("B2", "To Kill a Mockingbird", "Harper Lee", "Historical", False, "2025-11-01", 5)
    book3 = Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True, None, 3)
    book4 = Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4)
    book5 = Book("B5", "Pride and Prejudice", "Jane Austen", "Romance", True, None, 6)
    book6 = Book("B6", "The Hobbit", "J.R.R. Tolkein", "Fantasy", False, "2025-11-10", 8)
    book7 = Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1)
    book8 = Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age", False, "2025-11-12", 3)

    #Creating a list of all the objects
    book_list = [book1, book2, book3, book4, book5, book6, book7, book8]


    

    print("Welcome to the library. Please choose from the following options:")
    print("1. View available books")
    print("2. Search for a book")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. View overdue books")
    print("6. View top 3 most checked-out books")

    number = input("enter the number of your choice. ")
    if number == str(1):
        Book.print_available(book_list)
    if number == str(2):
        print(Book.search(book_list))
    if number == str(3):
        Book.checkout(book_list)
    if number == str(4):
        Book.return_book(book_list)
    if number == str(5):
        print(f"The following books are overdue:{view_overdue(book_list)}")     
    if number == str(6):
        Book.view_popular(book_list)

    


    pass
