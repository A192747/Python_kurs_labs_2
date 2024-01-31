class Person:
    def __init__(self, name: str, age: int):
        """
        Инициализирует объект Person.

        Аргументы:
            name (str): Имя человека.
            age (int): Возраст человека. Это должно быть неотрицательное целое число.

        Исключения:
            TypeError: Если возраст не является целым числом.
            ValueError: если возраст является отрицательным числом.
        """
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Возраст должен задаваться типом Int")
        if age < 0:
            raise ValueError("Значение возраста должно быть неотрицательным числом")
        self.age_ = age

    def __eq__(self, other) -> bool:
        """
        Проверяет, равны ли два объекта Person.

        Аргументы:
            other (Person): Объект другого человека для сравнения.

        Возврат:
            bool: True, если два объекта Person равны, в противном случае — False.
        """
        return self.age == other.age and self.name == other.name and self.__class__ == other.__class__

    @property
    def name(self) -> str:
        """str: Имя человека."""
        return self.name_

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Устанавливает новое имя человека.

        Аргументы:
            new_name (str): новое имя, которое нужно установить.

        Исключения:
            TypeError: Если новое имя не является строкой.
            ValueError: если новое имя содержит неалфавитные символы.
        """
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть типа String")
        for letter in new_name:
            if not letter.isalpha():
                raise ValueError("Имя должно содержать только буквы")
        self.name_ = new_name

    @property
    def age(self) -> int:
        """int: Возраст человека."""
        return self.age_

    def __str__(self) -> str:
        """str: Возвращает строковое представление объекта Person."""
        return f"Имя {self.name}. Возраст {self.age}"

    def __repr__(self) -> str:
        """str: Возвращает строковое представление объекта Person."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"


class Child(Person):
    def __init__(self, name: str, age: int, has_baby_teeth: bool):
        """
        Инициализирует дочерний объект, а затем поля данного класса.

        Аргументы:
            name (str): Имя ребенка.
            age (int): Возраст ребенка. Это должно быть неотрицательное целое число.
            has_baby_teeth (bool): True, если у ребенка есть молочные зубы, в противном случае — False.

        Поднимает:
            TypeError: если has_baby_teeth не является логическим значением.
        """
        super().__init__(name, age)
        self.has_baby_teeth = has_baby_teeth

    def __eq__(self, other) -> bool:
        """
        Это перегруженный метод, потому что для сравнения объектов класса Child, с новым полем has_baby_teeth,
        необходим новый метод сравнения. Он будет проверять есть ли поле has_baby_teeth или нет, и совпадают ли имя и
        возраст

        Проверяет, равны ли два дочерних объекта.

        Аргументы:
            Other (Child): Другой дочерний объект для сравнения.

        Возврат:
            bool: True, если два дочерних объекта равны, в противном случае — False.
        """
        return super().__eq__(other) and self.__class__ == other.__class__ and other.has_baby_teeth
    @property
    def has_baby_teeth(self) -> bool:
        """bool: True, если у ребенка есть молочные зубы, в противном случае False."""
        return self.has_baby_teeth_

    @has_baby_teeth.setter
    def has_baby_teeth(self, new_value) -> None:
        """
        Метод устанавливает наличие молочных зубов у ребенка.

        Аргументы:
            new_value (bool): новое значение, которое нужно установить.

        Поднимает:
            TypeError: Если новое значение не является логическим.
        """
        if not isinstance(new_value, bool):
            raise TypeError("Значение наличия или отсутствия молочных зубов должно быть типа Bool")
        self.has_baby_teeth_ = new_value

    def __repr__(self) -> str:
        """str: Возвращает строковое представление дочернего объекта."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, has_baby_teeth={self.has_baby_teeth!r})"


"""Перегруженный метод __eq__ в классе Child имеет документацию, 
которая объясняет, что метод используется для проверки равенства 
двух объектов Child. Это объяснение помогает понять, почему метод был перегружен.
Инкапсуляция в данном коде реализована с помощью свойств name, age и 
has_baby_teeth. Для каждого свойства есть методы-геттеры и методы-сеттеры, 
которые позволяют получать и устанавливать значения свойств. """

if __name__ == "__main__":
    person = Person("Alex", 22)
    child = Child("Andru", 5, True)
    print(child.__eq__(person))
    print(person.__eq__(child))
    print()
    print(child.__repr__())
    print(person.__repr__())

    child1 = Child("Alex", 22, True)
    print(child1.__eq__(person))
    print(person.__eq__(child1))
    print(child1.__repr__())
    print(person.__repr__())
    pass
