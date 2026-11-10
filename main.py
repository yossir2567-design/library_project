import files_1 as f


books = [{"id": 1, "name": "Harry Potter",             "author": "J.K. Rowling",   "year": 1997, "available": True},
         {"id": 2, "name": "The Hobbit",               "author": "J.R.R. Tolkien", "year": 1937, "available": True},
         {"id": 3, "name": "Clean Code",               "author": "Robert Martin",  "year": 2008, "available": False},
         {"id": 4, "name": "Atomic Habits",            "author": "James Clear",    "year": 2018, "available": True},
         {"id": 5, "name": "The Pragmatic Programmer", "author": "David Thomas",   "year": 1999, "available": False}
         ]


def main():
    
    while True:
        val = f.choose_search()

        if val == "1":
            f.display_books(books)
            continue

        elif val == "2":
            name = f.input_name()


            result = f.search_book(books, name)
            if result is None:
                mes = "The requested book was not found."
                f.print_message(mes)
            else:
                f.print_message(result)


        elif val == "3":
            name = f.input_name()
            author = f.input_author()
            year = f.input_year()

            result = f.add_book(books, name, author, year)
            if result == "succeeded":
                mes = "The book was added successfully!"
                f.print_message(mes)
            else:
                f.print_message(result)
            continue


        elif val == "4":
            book_id = f.input_id()
            result = f.borrow_book(books, book_id)
            if result == "succeeded":
                mes = "The book was successfully borrowed."
                f.print_message(mes)
            else:
                f.print_message(result)

            continue  
        
        elif val == "5":
            book_id = f.input_id()
            result = f.return_book(books, book_id)
            if result == "succeeded":
                mes = "The book was returned successfully."
                f.print_message(mes)
            else:
                f.print_message(result)
            continue


        elif val == "6":
            result = f.get_available_books(books)
            if result == None:
                mes = "No books available"
                f.print_message(mes)
            else:
                f.print_message(result)

            continue

        elif val == "7":
            author = f.input_author()


            result = f.get_books_by_author(books, author)
            if result is None:
                mes = "The requested book was not found."
                f.print_message(mes)
            else:
                f.print_message(result)
            continue

        elif val == "8":
            mes = "Logout successful"
            f.print_message(mes)
            break

if __name__ == "__main__":
    main()
