class Student:
    total_students_count = 0  # Общее количество студентов

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
        Student.total_students_count += 1  # Увеличиваем счетчик студентов

    def display_info(self):
        """Метод для вывода информации о студенте"""
        print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.average_grade()}")

    def add_grade(self, grade):
        """Метод для добавления оценки студенту"""
        self.grades.append(grade)

    def average_grade(self):
        """Метод для вычисления средней оценки"""
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


class GraduateStudent(Student):
    def __init__(self, name, age, thesis_topic):
        super().__init__(name, age)
        self.thesis_topic = thesis_topic  # Тема дипломной работы

    def display_info(self):
        """Переопределенный метод для вывода информации о выпускнике"""
        print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.average_grade()}, Тема диплома: {self.thesis_topic}")


def add_student():
    """Добавить студента"""
    name = input("Введите имя студента: ")
    age = int(input("Введите возраст студента: "))
    student_type = input("Обычный студент (S) или Выпускник (G)? ").strip().upper()

    if student_type == 'G':
        thesis_topic = input("Введите тему дипломной работы: ")
        student = GraduateStudent(name, age, thesis_topic)
    else:
        student = Student(name, age)

    students.append(student)
    print(f"Студент {name} добавлен.\n")


def add_grade_to_student():
    """Добавить оценку студенту"""
    name = input("Введите имя студента: ")
    found_student = next((student for student in students if student.name == name), None)

    if found_student:
        grade = float(input("Введите оценку: "))
        found_student.add_grade(grade)
        print(f"Оценка {grade} добавлена студенту {found_student.name}.\n")
    else:
        print(f"Студент с именем {name} не найден.\n")


def display_students_info():
    """Показать информацию обо всех студентах"""
    for student in students:
        student.display_info()


def sort_students_by_average_grade():
    """Сортировка студентов по средней оценке"""
    students.sort(key=lambda student: student.average_grade(), reverse=True)
    print("Студенты отсортированы по средней оценке.\n")


def show_total_students():
    """Показать общее количество студентов"""
    print(f"Общее количество студентов: {Student.total_students_count}\n")


students = []

while True:
    print("1. Добавить студента")
    print("2. Добавить оценку студенту")
    print("3. Показать информацию о студентах")
    print("4. Сортировка по средней оценке")
    print("5. Показать общее количество студентов")
    print("6. Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        add_grade_to_student()
    elif choice == '3':
        display_students_info()
    elif choice == '4':
        sort_students_by_average_grade()
    elif choice == '5':
        show_total_students()
    elif choice == '6':
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор, попробуйте снова.")
