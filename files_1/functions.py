from files_1 import printer as p
from rapidfuzz import fuzz, process



def choose_search():
    while True:
        mes = "========== ORDER MANAGER ==========\n 1. Display all books\n 2. Search book by name\n 3. Add new book\n 4. Borrow a book\n 5. Return a book\n 6. Display available booksn\n 7. Display books by author \n 8. Exit"
        p.print_message(mes)

        val = input("Choose an option: ")

        if val in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            return val
        else:
            mes = "Incorrect choice. Try again."
            p.print_message(mes)
        

def display_books(books):
    p.print_message(books)



def input_name():
    while True:
        name = input("Enter a name: ")
        if name:
            return name
        else:
            continue

def input_author():
    while True:
        author = input("Enter a author: ")
        if author:
            return author
        else:
            continue

def input_year():
    while True:
        year = input("Enter a year: ")
        check = check_valid_num(year)
        if check == True:
            positive = check_positive_num(year)
            if positive == True:
                return int(year)
            else:
                mes = "Error, enter the year as a number using digits only. try again."
                p.print_message(mes)
                continue

def input_id():
    while True:
        book_id = input("Enter a id: ")
        check = check_valid_num(book_id)
        if check == True:
            positive = check_positive_num(book_id)
            if positive == True:
                return int(book_id)
            else:
                mes = "Error, enter the id as a number using digits only. try again."
                p.print_message(mes)
                continue
        
def check_valid_num(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False

def check_positive_num(num):
    try:
        int(num) > 0
        return True
    except ValueError:
        return False


def search_book(books, name):
    result = find_best_book(books, name)
    return result
    




def find_best_book( books_list: list[dict], query: str, threshold: int = 60) -> dict | None:
    if not query.strip():
        return None

    result = process.extractOne(
        query.lower(),
        books_list,
        processor=lambda item: item["name"].lower() if isinstance(item, dict) else item,
        scorer=fuzz.WRatio,
        score_cutoff=threshold
    )

    if result:
        matched_book, score, index = result
        return matched_book
    return None


def add_book(books:list, name, author, year):
    try:
        for book in books:
            if book["name"] == name or book["author"] == author:
                return "Cannot add; the book or author already exists."

        new_book = {}
        new_book["id"] = get_next_book_id(books)
        new_book["name"] = name
        new_book["author"] = author
        new_book["year"] = year
        new_book["available"] = True

        books.append(new_book)
        return "succeeded"
    except:
        return "Adding the book failed!"

def get_next_book_id(books):
    return len(books) + 1



def borrow_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"] == True:
                book["available"] = False
                return "succeeded"
            else:
                return "The book is already checked out."
    return "The book is not in the database."


def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"] == False:
                book["available"] = True
                return "succeeded"
            else:
                return "The book already exists; it cannot be returned."
    return "The book is not listed in the database."


def get_available_books(books):
    result = list(filter(lambda p: p["available"] == True, books))
    if result == []:
        return None
    else:
        return result




def get_books_by_author(books, author):
    result = find_book_by_author(books, author)
    return result

def find_book_by_author(books_list: list[dict] ,query: str, threshold: int = 60) -> dict | None:
    if not query.strip():
        return None

    result = process.extractOne(
        query.lower(),
        books_list,
        processor=lambda item: item["author"].lower() if isinstance(item, dict) else item,
        scorer=fuzz.WRatio,
        score_cutoff=threshold
    )
    if result:
        matched_book, score, index = result
        return matched_book
    return None