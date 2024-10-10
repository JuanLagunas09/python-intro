class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"Libro {self.title} prestado")
        else:
            print("Libro no disponible")
    
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Libro {self.title} devuelto")
        else:
            print("Libro ya disponible")
    
    
# CLASE USUARIO
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.is_available:
            book.borrow_book()
            self.borrowed_books.append(book)
        else:
            print(f"Libro {book.title} no disponible")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"Libro {book.title} no lo tiene {self.name}")

# CLASE BIBLIOTECA
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Libro {book.title} añadido a la biblioteca")
    
    def add_user(self, user):
        self.users.append(user)
        print(f"Usuario {user.name} añadido a la biblioteca")
    
    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.is_available:
                print(f"{book.title} - {book.author}")
                
    def show_borrowed_books(self):
        print("Libros prestados:")
        for book in self.books:
            if not book.is_available:
                print(f"{book.title} - {book.author}")
    
    def show_books(self):
        print("Libros:")
        for book in self.books:
            print(f"{book.title} - {book.author} - {'Disponible' if book.is_available else 'No disponible'}")
            
    def show_users(self):
        print("Usuarios:")
        for user in self.users:
            print(f"{user.name} - {user.user_id}")
            
# Se crea la biblioteca        
biblioteca = Library()
# Se crean los objetos de la clase Book     
book_1 = Book("El principito", "Antoine de Saint-Exupéry")
book_2 = Book("El señor de los anillos", "J.R.R. Tolkien")
book_3 = Book("Cien años de soledad", "Gabriel García Márquez")
book_4 = Book("Don Quijote de la Mancha", "Miguel de Cervantes")
book_5 = Book("La Odisea", "Homero")
# Se crean los objetos de la clase User
user_1 = User("Juan", 1)
user_2 = User("Ana", 2)
user_3 = User("Pedro", 3)


biblioteca.add_book(book_1)
biblioteca.add_book(book_2)
biblioteca.add_book(book_3)
biblioteca.add_book(book_4)
biblioteca.add_book(book_5)
print("---------------")
biblioteca.add_user(user_1)
biblioteca.add_user(user_2)
biblioteca.add_user(user_3)
print("---------------")
biblioteca.show_books()
print("---------------")
biblioteca.show_users()
print("---------------")
user_1.borrow_book(book_1)
user_2.borrow_book(book_1)
user_1.return_book(book_1)
user_2.borrow_book(book_1)
print("---------------")
biblioteca.show_borrowed_books()