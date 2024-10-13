class Book:
    total_available_books = 0  # Общее количество доступных книг

    def __init__(self, title, author, year, pages):
        """
        Инициализация объекта книги с ее названием, автором, годом издания и количеством страниц.
        Устанавливается доступность книги и увеличивается счетчик доступных книг.
        """
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.available = True  # По умолчанию книга доступна
        Book.total_available_books += 1  # Увеличиваем общее количество доступных книг

    def display_info(self):
        """
        Отображает информацию о книге, включая ее доступность.
        """
        availability = "Доступна" if self.available else "Не доступна"
        print(f"\nСписок данных:\
            \n1 - Название               - {self.title}\
            \n2 - Автор                  - {self.author}\
            \n3 - Год издания            - {self.year}\
            \n4 - Количество страниц     - {self.pages}\
            \n5 - Доступность            - {availability}")

    def borrow_book(self):
        """
        Устанавливает статус книги как "занята" и уменьшает счетчик доступных книг.
        """
        if self.available:
            self.available = False
            Book.total_available_books -= 1  # Уменьшаем общее количество доступных книг
            print(f"Вы взяли книгу: {self.title}")
        else:
            print(f"Вы не можете взять книгу '{self.title}', так как она недоступна.")

    def return_book(self):
        """
        Устанавливает статус книги как "доступна" и увеличивает счетчик доступных книг.
        """
        if not self.available:
            self.available = True
            Book.total_available_books += 1  # Увеличиваем общее количество доступных книг
            print(f"Книгу '{self.title}' вернули")
        else:
            print(f"Книга '{self.title}' уже возвращена.")

    def __str__(self):
        """
        Возвращает строковое представление объекта книги.
        """
        return f"Книга '{self.title}' от {self.author}, {self.year} год, {self.pages} страниц"

    def __add__(self, other):
        """
        Добавляет указанное количество страниц к книге.
        """
        if isinstance(other, int):
            self.pages += other
        else:
            print("Укажите количество страниц в виде целого числа.")
        return self

    def __sub__(self, other):
        """
        Уменьшает количество страниц книги на указанное значение.
        """
        if isinstance(other, int) and self.pages > other:
            self.pages -= other
        else:
            print("Укажите количество страниц в виде целого числа.")
        return self

    @staticmethod
    def total_books():
        """
        Отображает общее количество доступных книг.
        """
        print(f"Всего книг в библиотеке: {Book.total_available_books}")


class DigitalBook(Book):
    def __init__(self, title, author, year, pages, file_format):
        """
        Инициализация объекта цифровой книги с добавлением формата файла.
        """
        super().__init__(title, author, year, pages)
        self.file_format = file_format

    def display_info(self):
        """
        Отображает информацию о цифровой книге, включая формат файла.
        """
        super().display_info()
        print(f"Формат: {self.file_format}")

    def download_book(self):
        """
        Возвращает строку, указывающую на возможность скачивания книги.
        """
        return f"Книга '{self.title}' от {self.author}, {self.year} год, {self.pages} страниц, доступна для скачивания в формате: {self.file_format}"

    def __str__(self):
        """
        Возвращает строковое представление объекта цифровой книги.
        """
        return (f'\nЭлектронная книга: {self.title}, '
                f'Автор: {self.author}, '
                f'Год: {self.year}, '
                f'Страниц: {self.pages}, '
                f'Формат: {self.file_format}').strip()


library = []  # Список для хранения всех книг

def add_book():
    """
    Добавляет физическую или цифровую книгу в библиотеку.
    """
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
    """
    Позволяет пользователю взять физическую книгу.
    """
    title = input("Введите название книги, которую хотите взять: ")
    for book in library:
        if isinstance(book, Book) and not isinstance(book, DigitalBook) and book.title == title:
            book.borrow_book()
            return
    print(f"Книга '{title}' не найдена или недоступна для взятия.")

def return_book():
    """
    Функция для возврата физической книги.
    """
    title = input("Введите название книги, которую хотите вернуть: ")  # Запрос названия книги
    for book in library:  # Цикл по всем книгам в библиотеке
        # Проверка, что книга физическая и была взята
        if isinstance(book, Book) and not isinstance(book, DigitalBook) and book.title == title:
            book.return_book()  # Вызов метода для возврата книги
            return
    print(f"Книга '{title}' не найдена среди взятых.")  # Сообщение, если книга не найдена

def download_book():
    """
    Функция для скачивания цифровой книги.
    """
    title = input("Введите название книги, которую хотите скачать: ")  # Запрос названия книги
    for book in library:  # Цикл по всем книгам в библиотеке
        # Проверка, что книга цифровая
        if isinstance(book, DigitalBook) and book.title == title:
            book.download_book()  # Вызов метода для скачивания книги
            print(f"Цифровая книга '{title}' скачана.")
            return
    print(f"\nЦифровая книга '{title}' не найдена.")  # Сообщение, если книга не найдена

def show_book_info():
    """
    Функция для отображения информации о книге.
    """
    title = input("Введите название книги: ")  # Запрос названия книги
    for book in library:  # Цикл по всем книгам в библиотеке
        if book.title == title:  # Проверка, найдено ли название
            book.display_info()  # Вызов метода для отображения информации о книге
            return
    print(f"\nКнига '{title}' не найдена.")  # Сообщение, если книга не найдена

def show_all_books():
    """
    Функция для отображения всех книг в библиотеке.
    """
    if library:  # Проверка, есть ли книги в библиотеке
        for book in library:  # Цикл по всем книгам
            print(book)  # Вывод книги
    else:
        print("\nВ библиотеке нет книг.")  # Сообщение, если книг нет

def show_book_str():
    """
    Функция для отображения строкового представления книги.
    """
    title = input("Введите название книги: ")  # Запрос названия книги
    for book in library:  # Цикл по всем книгам в библиотеке
        if book.title == title:  # Проверка, найдено ли название
            print(str(book))  # Вывод строкового представления книги
            return
    print(f"\nКнига '{title}' не найдена.")  # Сообщение, если книга не найдена

# Функция main() запускает взаимодействие с пользователем.
def main():
    """
    Основная функция, обеспечивающая работу программы с пользователем.
    """
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
