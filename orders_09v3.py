"""Импорт Abcstactmethod"""

from abc import ABC, abstractmethod


class OrderBase(ABC):
    """Абстрактный базовый класс для заказов."""

    total_orders_count = 0

    def __init__(self, order_number):
        self.order_number = order_number
        self.status = "Новый"
        OrderBase.total_orders_count += 1

    @abstractmethod
    def display_info(self):
        """Абстрактный метод для отображения информации о заказе."""

    @staticmethod
    def total_orders():
        """Вывод общего количества заказов."""
        print(f"Общее количество заказов: {OrderBase.total_orders_count}")

    def change_status(self, status):
        """Изменение статуса заказа."""
        self.status = status

    def __str__(self):
        return f"Заказ №{self.order_number}, Статус: {self.status}"


class Order(OrderBase):
    """Класс обычного заказа."""

    def __init__(self, order_number):
        super().__init__(order_number)
        self.dishes = []

    def add_dish(self, dish):
        """Добавление блюда в заказ."""
        self.dishes.append(dish)

    def display_info(self):
        """Отображение информации о заказе."""
        info = (
            f"Заказ №{self.order_number}\n"
            f"Статус: {self.status}\n"
            f"Блюда: {', '.join(self.dishes)}"
        )
        print(info)

    def __str__(self):
        return f"Заказ №{self.order_number}, Статус: {self.status}, " \
               f"Блюда: {', '.join(self.dishes)}"

    def __add__(self, dish):
        """Добавление блюда через оператор +."""
        self.add_dish(dish)
        return self

    def __sub__(self, dish):
        """Удаление блюда через оператор -."""
        if dish in self.dishes:
            self.dishes.remove(dish)
        return self


class DeliveryOrder(OrderBase):
    """Класс заказа с доставкой."""

    def __init__(self, order_number, delivery_address, delivery_time):
        super().__init__(order_number)
        self.delivery_address = delivery_address
        self.delivery_time = delivery_time
        self.dishes = []

    def add_dish(self, dish):
        """Добавление блюда в заказ с доставкой."""
        self.dishes.append(dish)

    def display_info(self):
        """Отображение информации о заказе с доставкой."""
        super().display_info()
        print(
            f"Адрес доставки: {self.delivery_address}\n"
            f"Время доставки: {self.delivery_time}\n"
            f"Блюда: {', '.join(self.dishes)}"
        )

    def __str__(self):
        return (
            f"Заказ №{self.order_number}, Статус: {self.status}, "
            f"Адрес доставки: {self.delivery_address}, "
            f"Время доставки: {self.delivery_time}, "
            f"Блюда: {', '.join(self.dishes)}"
        )

    def __add__(self, dish):
        """Добавление блюда через оператор +."""
        self.add_dish(dish)
        return self

    def __sub__(self, dish):
        """Удаление блюда через оператор -."""
        if dish in self.dishes:
            self.dishes.remove(dish)
        return self


def main():
    """Основная функция программы."""
    orders = []

    while True:
        print("\nМеню:")
        print("1. Создать обычный заказ")
        print("2. Создать заказ с доставкой")
        print("3. Добавить блюдо в заказ")
        print("4. Изменить статус заказа")
        print("5. Показать информацию о заказе")
        print("6. Показать общее количество заказов")
        print("7. Показать все заказы")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            order_number = len(orders) + 1
            order = Order(order_number)
            orders.append(order)
            print(f"Создан обычный заказ №{order_number}.")

        elif choice == "2":
            order_number = len(orders) + 1
            delivery_address = input("Введите адрес доставки: ")
            delivery_time = input("Введите время доставки: ")
            delivery_order = DeliveryOrder(
                order_number, delivery_address, delivery_time
            )
            orders.append(delivery_order)
            print(f"Создан заказ с доставкой №{order_number}.")

        elif choice == "3":
            order_number = int(input("Введите номер заказа: "))
            dish = input("Введите название блюда: ")
            if 0 < order_number <= len(orders):
                orders[order_number - 1].add_dish(dish)
                print(f"Блюдо '{dish}' добавлено в заказ №{order_number}.")
            else:
                print("Заказ не найден.")

        elif choice == "4":
            order_number = int(input("Введите номер заказа: "))
            status = input("Введите новый статус заказа: ")
            if 0 < order_number <= len(orders):
                orders[order_number - 1].change_status(status)
                print(f"Статус заказа №{order_number} изменен на '{status}'.")
            else:
                print("Заказ не найден.")

        elif choice == "5":
            order_number = int(input("Введите номер заказа: "))
            if 0 < order_number <= len(orders):
                orders[order_number - 1].display_info()
            else:
                print("Заказ не найден.")

        elif choice == "6":
            OrderBase.total_orders()

        elif choice == "7":
            for order in orders:
                print(order)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
