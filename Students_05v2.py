class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def give_grade(self, grade):
        self.grades.append(grade)

    def display_info(self):
        averge_grade = self.give_averge_grade()
        print(f"Студент: {self.name}, Возраст: {self.age}, Средняя оценка: {averge_grade:.2f}")

    def give_averge_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0


class GraduateStudent(Student):
    def __init__(self, name, age, topic_diploma):
        super().__init__(name, age)
        self.topic_diploma = topic_diploma

    def display_info(self):
        averge_grade = self.give_averge_grade()
        print(f"Выпускник: {self.name}, Возраст: {self.age}, "
              f"Средняя оценка: {averge_grade:.2f}, Тема дипломной работы: {self.topic_diploma}")


def main():
    students = []

    while True:
        print("\nМеню:\
            \n1 - Добавить студента\
            \n2 - Добавить оценку студенту\
            \n3 - Добавить тему дипломной работы (для выпускников)\
            \n4 - Показать информацию о студентах\
            \n5 - Сортировка по средней оценке\
            \n6 - Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            type_of_student = input("Введите тип студента (обычный/выпускник): ").strip().lower()
            if type_of_student == 'выпускник' or type_of_student == 'обычный':
                name = input("Введите имя студента: ").strip()
                age = int(input("Введите возраст студента: "))
                if type_of_student == 'выпускник':
                    topic_diploma = input("Введите тему дипломной работы: ")
                    students.append(GraduateStudent(name, age, topic_diploma))
                else:
                    students.append(Student(name, age))
            else: 
                print("Неправильно введен тип студента.")

        elif choice == '2':
            name = input("Введите имя студента: ").strip()
            grade = float(input("Введите оценку: "))
            for student in students:
                if student.name == name:
                    student.give_grade(grade)
                    print(f"Оценка {grade} добавлена студенту {name}.")
                    break
            else:
                print("Студент не найден.")

        elif choice == '3':
            name = input("Введите имя выпускника: ").strip()
            topic_diploma = input("Введите тему дипломной работы: ")
            for student in students:
                if isinstance(student, GraduateStudent) and student.name == name:
                    student.topic_diploma = topic_diploma
                    print(f"Тема дипломной работы обновлена для {name}.")
                    break
            else:
                print("Выпускник не найден.")

        elif choice == '4':
            for student in students:
                student.display_info()

        elif choice == '5':
            sorted_students = sorted(students, key=lambda s: s.give_averge_grade(), reverse=True)
            print("Студенты по средней оценке:")
            for student in sorted_students:
                student.display_info()

        elif choice == '6':
            print("Выход...")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите цифру из списка.")


if __name__ == "__main__":
    main()
