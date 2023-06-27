from src.item import Item

class MixinLan():
    lan = "EN"
    def __init__(self):
        self.__language = MixinLan.lan

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLan):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


