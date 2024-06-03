# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы,
# помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя
# из системы.
#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
#('user' для обычных сотрудников).
#2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).


class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.access = "user"

    def admin_access(self):
        self.access = "admin"

    def user_access(self):
        self.access = "user"

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__staff = []

    def add_user(self, id, name):
        unit = User(id, name)
        self.__staff.append(unit)
        print(f"Пользователь {name} добавлен в штат сотрудников")

    def get_users(self):
        for unit in self.__staff:
            print(f"{unit.id}. {unit.name}. Уровень доступа: {unit.access}")

    def change_access_admin(self, id):
        for user in self.__staff:
            if user.id == id:
                user.admin_access()
                print(f"Уровень доступа пользователя {id}. {user.name} изменен на 'admin'")
            elif user.id != id:
                print(f"Пользователя {id} нет в штате сотрудников")
                break

    def change_access_user(self, id):
        for user in self.__staff:
            if user.id == id:
                user.user_access()
                print(f"Уровень доступа пользователя {id}. {user.name} возвращен на 'user'")

    def remove_user(self, id):
        for user in self.__staff:
            if user.id == id:
                self.__staff.remove(user)
                print(f"Пользователь {id}. {user.name} удален из штата сотрудников")
            elif user.id != id:
                print(f"Пользователя {id} нет в штате сотрудников")
                break


admin = Admin(0, "Администратор")
admin.add_user(1, "Сергей")
admin.add_user(2, "Алиса")
admin.add_user(3, "Олег")
admin.add_user(4, "Евгения")
admin.get_users()
admin.change_access_admin(6)
admin.change_access_admin(2)
admin.get_users()
admin.remove_user(3)
admin.get_users()
admin.change_access_user(2)
admin.get_users()

