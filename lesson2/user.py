"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False
при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:
    """Класс пользователя"""

    def __init__(self, name, password: str):
        self.__name = name
        self.__password = password
        self._is_admin = False
        self._is_logged_in = None

    @property
    def name(self):
        return self.__name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pswd):
        self.__password = new_pswd

    @property
    def is_admin(self):
        return self._is_admin

    def login(self, password):
        self._is_logged_in = True if self.__password == password else False
        return self._is_logged_in

    def logout(self):
        if self._is_logged_in:
            self._is_logged_in = False
        return self._is_logged_in

# код для проверки


user1 = User("Alice", "qwerty")

# print(user1.name)  # Alice
# print(user1.password)  # qwerty
# print(user1.is_admin)  # False

# user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
# print(user1.is_admin)  # True

print(user1.login("qwerty"))  # True
user1.logout()
print(user1._is_logged_in)
