import doctest
class Ball:
    def __init__(self, radius: float, pressure: float):
        """
        Создание и подготовка к работе объекта "Мяч"

        :param radius: Радиус мяча (в см)
        :param pressure: Давление в мяче (в Па)

        Примеры:
        >>> ball1 = Ball(10, 5)  # инициализация экземпляра класса
        >>> ball2 = Ball(100, 1)
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус мяча должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус мяча должен быть положительным числом")
        self.radius = radius

        if not isinstance(pressure, (int, float)):
            raise TypeError("Давление в мяче должно быть int или float")
        if pressure < 0:
            raise ValueError("Давление в мяче не должно быть отрицательным числом")
        self.pressure = pressure

    def increase_pressure(self, value: float) -> None:
        """
        Функция, которая увеличивает давление в мяче
        :param value: значение добавляемое к текущему значению pressure
        :raise ValueError: Если передаваемое значение value < 0, то вызываем ошибку

        Примеры:
        >>> ball = Ball(10, 5)
        >>> ball.increase_pressure(5)
        """
        ...

    def destruct_ball(self) -> None:
        """
        Функция, которая сдувает/уничтожает мяч

        Примеры:
        >>> ball = Ball(10, 5)
        >>> ball.destruct_ball()
        """
        ...


class Tube:
    def __init__(self, radius: float, length: float):
        """
        Создание и подготовка к работе объекта "Труба"

        :param radius: Радиус трубы (в см)
        :param pressure: Длинна трубы (в см)

        Примеры:
        >>> tube1 = Tube(10, 5)  # инициализация экземпляра класса
        >>> tube2 = Tube(100, 1)
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус трубы должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус трубы должен быть положительным числом")
        self.radius = radius

        if not isinstance(length, (int, float)):
            raise TypeError("Длинна трубы должна быть int или float")
        if length <= 0:
            raise ValueError("Длинна трубы должна быть положительным числом")
        self.pressure = length

    def is_longer_than(self, value: float) -> bool:
        """
        Функция, которая проверяет больше ли длинна трубы, чем определенное значение

        :param value: значение, с которым сравнивается текущая length трубы

        Примеры:
        >>> tube1 = Tube(10, 5)
        >>> tube1.is_longer_than(1)
        """
        ...

    def divide_the_radius_by_two(self) -> None:
        """
        Функция, делит значение текущего радиуса на 2

        Примеры:
        >>> tube1 = Tube(10, 5)
        >>> tube1.divide_the_radius_by_two()
        """
        ...


class Keyboard:
    def __init__(self, count_of_buttons: int, is_working: bool):
        """
        Создание и подготовка к работе объекта "Клавиатура"

        :param count_of_buttons: Количество клавиш у клавиатуры
        :param is_working: Рабочая ли клавиатура на данный момент

        Примеры:
        >>> keyboard1 = Keyboard(10, True)  # инициализация экземпляра класса
        >>> keyboard2 = Keyboard(34, False)
        """
        if not isinstance(count_of_buttons, int):
            raise TypeError("Количество кнопок должно быть типа int")
        if count_of_buttons < 0:
            raise ValueError("Количество кнопок не должно быть отрицательным числом")
        self.count_of_buttons = count_of_buttons

        if not isinstance(is_working, bool):
            raise TypeError("Работоспособность клавиатуры должна быть bool")

        self.is_working = is_working

    def repair(self) -> None:
        """
        Функция, которая чинит клавиатуру (is_warking == true), если она была сломана (is_warking == false)

        Примеры:
        >>> keyboard3 = Keyboard(34, False)
        >>> keyboard3.repair()
        """
        ...

    def add_buttons(self, value: int) -> None:
        """
        Функция, которая увеличивает кол-во клавиш в клавиатуре

        :param value: значение, на которое должно увеличиться кол-во клавиш
        :raise ValueError: Если передаваемое значение value < 0, то вызываем ошибку
        :raise TypeError: Если передали не int

        Примеры:
        >>> keyboard3 = Keyboard(10, True)
        >>> keyboard3.add_buttons(5)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
