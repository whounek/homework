# Определяем класс Student для создания объектов студентов
class Student:
    def __init__(self, name, age):
        """
        Инициализация объекта студента с его именем и возрастом.
        Создается пустой список для хранения оценок студента.
        """
        self.name = name
        self.age = age
        self.grades = []

    def give_grade(self, grade):
        """
        Добавляет оценку в список оценок студента, если она находится в диапазоне от 0 до 5.
        Если оценка некорректна, выводит сообщение об ошибке.
        """
        if 0 <= grade <= 5:
            self.grades.append(grade)
            print(f"Оценка '{grade}' успешно добавлена студенту '{self.name}'")
        else:
            print("Ошибка: оценка должна быть в диапазоне от 0 до 5")

    def display_info(self):
        """
        Отображает информацию о студенте: имя, возраст и среднюю оценку.
        """
        averge_grade = self.give_averge_grade()
        print(
            f"Студент: {self.name}, Возраст: {self.age}, Средняя оценка: {averge_grade:.2f}"
        )

    def give_averge_grade(self):
        """
        Вычисляет и возвращает среднюю оценку студента.
        Если у студента нет оценок, возвращается 0.
        """
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0


# Определяем класс GraduateStudent для создания объектов выпускников (наследует класс Student)
class GraduateStudent(Student):
    def __init__(self, name, age, topic_diploma):
        """
        Инициализация объекта выпускника с его именем, возрастом и темой дипломной работы.
        Используется конструктор базового класса Student.
        """
        super().__init__(name, age)
        self.topic_diploma = topic_diploma

    def display_info(self):
        """
        Отображает информацию о выпускнике, включая тему дипломной работы.
        """
        averge_grade = self.give_averge_grade()
        print(
            f"Выпускник: {self.name}, Возраст: {self.age}, "
            f"Средняя оценка: {averge_grade:.2f}, Тема дипломной работы: {self.topic_diploma}"
        )


students = []  # Список для хранения объектов студентов и выпускников

# Основная функция, управляющая взаимодействием с пользователем
def main():
    """
    Основная функция, запускающая интерфейс взаимодействия с пользователем.
    Реализует меню для управления данными о студентах и выпускниках.
    """
    while True:
        """
        Цикл для отображения меню и выполнения выбранных пользователем действий.
        """
        print(
            "\nМеню:\
            \n1 - Добавить студента\
            \n2 - Добавить оценку студенту\
            \n3 - Добавить тему дипломной работы (для выпускников)\
            \n4 - Показать информацию о студентах\
            \n5 - Сортировка по средней оценке\
            \n6 - Выход"
        )

        choice = input("Выберите опцию: ")  # Запрос у пользователя выбора действия

        if choice == "1":
            """
            Добавление нового студента или выпускника в зависимости от типа.
            """
            type_of_student = (
                input("Введите тип студента (обычный/выпускник): ").strip().lower()
            )
            if type_of_student == "выпускник" or type_of_student == "обычный":
                name = input("Введите имя студента: ").strip()
                age = int(input("Введите возраст студента: "))
                if type_of_student == "выпускник":
                    topic_diploma = input("Введите тему дипломной работы: ")
                    students.append(GraduateStudent(name, age, topic_diploma))
                else:
                    students.append(Student(name, age))
            else:
                print("Неправильно введен тип студента.")

        elif choice == "2":
            """
            Добавление оценки существующему студенту.
            """
            name = input("Введите имя студента: ").strip()
            try:
                grade = float(input("Введите оценку (от 0 до 5): "))
            except ValueError:
                print("Ошибка: оценка должна быть числом")
                continue

            for student in students:
                if student.name == name:
                    student.give_grade(grade)
                    print(f"Оценки студента {student.name}: {student.grades}")
                    break
            else:
                print("Студент не найден.")

        elif choice == "3":
            """
            Добавление или обновление темы дипломной работы для выпускника.
            """
            name = input("Введите имя выпускника: ").strip()
            topic_diploma = input("Введите тему дипломной работы: ")
            for student in students:
                if isinstance(student, GraduateStudent) and student.name == name:
                    student.topic_diploma = topic_diploma
                    print(f"Тема дипломной работы обновлена для {name}.")
                    break
            else:
                print("Выпускник не найден.")

        elif choice == "4":
            """
            Отображение информации обо всех студентах и выпускниках.
            """
            for student in students:
                student.display_info()

        elif choice == "5":
            """
            Сортировка студентов по средней оценке в порядке убывания.
            """
            sorted_students = sorted(
                students, key = lambda s: s.give_averge_grade(), reverse = True
            )
            print("Студенты по средней оценке:")
            for student in sorted_students:
                student.display_info()

        elif choice == "6":
            """
            Завершение работы программы.
            """
            print("Выход...")
            break

        else:
            """
            Обработка некорректного выбора пользователя.
            """
            print("Некорректный ввод. Пожалуйста, выберите цифру из списка.")


# Проверка, что программа запускается непосредственно, а не импортируется как модуль
if __name__ == "__main__":
    main()
