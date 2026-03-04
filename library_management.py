# Library Management System
# Developer2 Branch - Added book returning feature

def add_book(library, book_name):
    library.append(book_name)
    print(f"Book '{book_name}' added to the library.")
    return library

def remove_book(library, book_name):
    if book_name in library:
        library.remove(book_name)
        print(f"Book '{book_name}' removed from the library.")
    else:
        print(f"Book '{book_name}' not found.")
    return library

def search_book(library, book_name):
    if book_name in library:
        print(f"Book '{book_name}' is available.")
    else:
        print(f"Book '{book_name}' is not available.")

def display_books(library):
    if library:
        print("Books available in library:")
        for book in library:
            print(f" - {book}")
    else:
        print("Library is empty.")

def count_books(library):
    print(f"Total books in library: {len(library)}")
    return len(library)

# Developer2 added this new function
def return_book(library, book_name, member_name):
    library.append(book_name)
    print(f"Book '{book_name}' returned by {member_name} successfully.")
    return library

# Main
if __name__ == "__main__":
    library = []
    library = add_book(library, "Python Basics")
    library = add_book(library, "Git & GitHub Guide")
    library = add_book(library, "Data Structures")
    display_books(library)
    count_books(library)
    search_book(library, "Python Basics")
    library = remove_book(library, "Git & GitHub Guide")
    library = return_book(library, "Python Basics", "Shrikant")
    display_books(library)
