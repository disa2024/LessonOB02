class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__access = "user"

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def access(self):
        return self.__access

    def set_access(self, access_level):
        self.__access = access_level

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__staff = []

    def add_user(self, user):
        self.__staff.append(user)
        print(f"Пользователь {user.name} добавлен в штат сотрудников")

    def get_users(self):
        for user in self.__staff:
            print(f"{user.id}. {user.name}. Уровень доступа: {user.access}")

    def change_access(self, id, access_level):
        user = self.__find_user(id)
        if user:
            user.set_access(access_level)
            print(f"Уровень доступа пользователя {id}. {user.name} изменен на '{access_level}'")
        else:
            print(f"Пользователя {id} нет в штате сотрудников")

    def remove_user(self, id):
        user = self.__find_user(id)
        if user:
            self.__staff.remove(user)
            print(f"Пользователь {id}. {user.name} удален из штата сотрудников")
        else:
            print(f"Пользователя {id} нет в штате сотрудников")

    def __find_user(self, id):
        for user in self.__staff:
            if user.id == id:
                return user


# Пример использования:
admin = Admin(0, "Администратор")
user1 = User(1, "Сергей")
user2 = User(2, "Алиса")
user3 = User(3, "Олег")
user4 = User(4, "Евгения")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)

admin.get_users()

admin.change_access(9, "admin")
admin.get_users()

admin.remove_user(3)
admin.get_users()

admin.change_access(2, "user")
admin.get_users()