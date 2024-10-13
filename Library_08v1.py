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
        print(f"\nСписок данных:\
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
        return f"Книга '{self.title}' от {self.author}, {self.year} год, {self.pages} страниц"

    def __add__(self, other):
        if isinstance(other, int):
            self.pages += other
        else:
            print("Укажите количество страниц в виде целого числа.")
        return self

    def __sub__(self, other):
        if isinstance(other, int) and self.pages > other:
            self.pages -= other
        else:
            print("Укажите количество страниц в виде целого числа.")
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

    def download_book(self):
        return f"Книга '{self.title}' от {self.author}, {self.year} год, {self.pages} страниц, доступна для скачивания в формате: {self.file_format}"

    def __str__(self):
            return (f'\nЭлектронная книга: {self.title}, '
                    f'Автор: {self.author}, '
                    f'Год: {self.year}, '
                    f'Страниц: {self.pages}, '
                    f'Формат: {self.file_format}').strip()
library = []

def add_book():
    book_type = input("Введите тип книги (физическая или цифровая): ").strip().lower()
    if book_type == "физическая" or book_type == 'цифровая':
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")

        while True:
            try:
                year = int(input("Введите год издания книги: "))
                if year <= 2024:
                    break
            except ValueError:
                print("Пожалуйста, введите корректный год (числом).")

        while True:
            try:
                pages = int(input("Введите количество страниц: "))
                if pages > 0:
                    break
            except ValueError:
                print("Пожалуйста, введите корректное количество страниц (число).")

    if book_type == "физическая":
            library.append(Book(title, author, year, pages))
            print(f"\nФизическая книга '{title}' добавлена в библиотеку.")

    elif book_type == "цифровая":
            file_format = input("Введите формат файла (PDF, EPUB и т.д.): ")
            library.append(DigitalBook(title, author, year, pages, file_format))
            print(f"\nЦифровая книга '{title}' добавлена в библиотеку.")
    else:
        print("Неверный тип книги!")

def take_book():
    title = input("Введите название книги, которую хотите взять: ")
    for book in library:
        if isinstance(book, Book) and not isinstance(book, DigitalBook) and book.title == title:
            book.borrow_book()
            return
    print(f"Книга '{title}' не найдена или недоступна для взятия.")

def return_book():
    title = input("Введите название книги, которую хотите вернуть: ")
    for book in library:
        if isinstance(book, Book) and not isinstance(book, DigitalBook) and book.title == title:
            book.return_book()
            return
    print(f"Книга '{title}' не найдена среди взятых.")

def download_book():
    title = input("Введите название книги, которую хотите скачать: ")
    for book in library:
        if isinstance(book, DigitalBook) and book.title == title:
            book.download_book()
            print(f"Цифровая книга '{title}' скачана.")
            return
    print(f"\nЦифровая книга '{title}' не найдена.")

def show_book_info():
    title = input("Введите название книги: ")
    for book in library:
        if book.title == title:
            book.display_info()
            return
    print(f"\nКнига '{title}' не найдена.")

def show_all_books():
    if library:
        for book in library:
            print(book)
    else:
        print("\nВ библиотеке нет книг.")

def show_book_str():
    title = input("Введите название книги: ")
    for book in library:
        if book.title == title:
            print(str(book))
            return
    print(f"\nКнига '{title}' не найдена.")

def main():
    while True:
        print("\nМеню:\
        \n1 - Добавить книгу\
        \n2 - Взять физическую книгу\
        \n3 - Вернуть физическую книгу\
        \n4 - Скачать цифровую книгу\
        \n5 - Показать информацию о книге\
        \n6 - Показать список всех книг\
        \n7 - Показать общее количество книг\
        \n8 - Показать строковое представление книги\
        \n0 - Выйти")

        command = input("\nВыберите опцию: ").strip()

        if command == "1":
            add_book()
        elif command == "2":
            take_book()
        elif command == "3":
            return_book()
        elif command == "4":
            download_book()
        elif command == "5":
            show_book_info()
        elif command == "6":
            show_all_books()
        elif command == "7":
            Book.total_books()
        elif command == "8":
            show_book_str()
        elif command == "0":
            print("Выход...")
            break
        else:
            print("Неверная команда, попробуйте снова.")

if __name__ == "__main__":
    main()