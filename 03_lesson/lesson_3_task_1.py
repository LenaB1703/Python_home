from user import User

#создание экземпляра класса User
my_user = User("Иван", "Иванов")

#вызываем метод у объекта
print(my_user.get_first_name())
print(my_user.get_last_name())