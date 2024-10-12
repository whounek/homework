class Book:
    total_available_books = 0  

    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.available = True  
        Book.total_available_books += 1  


    def display_info(self):
        availability = "Доступна" if self.available else "Не доступна"
        print(f"\nСписок:\
            \n1 - Название               - {self.title}\
            \n2 - Автор                  - {self.author}\
            \n3 - Год издания            - {self.year}\
            \n4 - Количество страниц     - {self.pages}\
            \n5 - Доступность            - {availability}")

        
    def borrow_book(self):
        if self.available:
            self.available = False
            Book.total_available_books -= 1  
            print(f"Вы взяли книгу: {self.title}")
        else:
            print(f"Вы не можете взять книгу '{self.title}',так как она недоступна.")

    def return_book(self):
        if not self.available:
            self.available = True
            Book.total_available_books += 1  
            print(f"Книгу '{self.title}' вернули")
        else:
            print(f"Книга '{self.title}' уже возвращена.")

    def __str__(self):
        return f"Книга {self.title} от {self.author}, {self.year}, {self.pages} страниц"

    def __add__(self, other):
        if isinstance(other, int):
            self.pages += other
        return self

    def __sub__(self, other):
        if isinstance(other, int) and self.pages > other:
            self.pages -= other
        return self

    @staticmethod
    def total_books():
        print(f"Всего книг в библиотеке: {Book.total_available_books}")


class DigitalBook(Book):
    def __init__(self, title, author, year, pages, file_format):
        super().__init__(title, author, year, pages)
        self.file_format = file_format

    def display_info(self):
        super().display_info()
        print(f"Формат: {self.file_format}")

    def __str__(self):
        return f"Книга {self.title} от {self.author}, {self.year}, {self.pages} страниц, формат: {self.file_format}"


# Пример использования функционала
physical_book = Book("1984", "George Orwell", 1949, 328)
digital_book = DigitalBook("Brave New World", "Aldous Huxley", 1932, 268, "PDF")

# Показать информацию о книге
physical_book.display_info()
print()
digital_book.display_info()

# Взять и вернуть физическую книгу
physical_book.borrow_book()
physical_book.return_book()

# Показать строковое представление книги
print(str(physical_book))
print(str(digital_book))

# Изменение количества страниц
physical_book += 20
digital_book -= 50
print(f"Updated pages in '{physical_book.title}': {physical_book.pages}")
print(f"Updated pages in '{digital_book.title}': {digital_book.pages}")

# Показать общее количество книг в библиотеке
Book.total_books()
