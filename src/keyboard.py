from src.item import Item

class MixinLan():
    lan = "EN"
    def __init__(self):
        self.language = MixinLan.lan

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self

    @property
    def language(self):
        return self.language


class KeyBoard(Item, MixinLan):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


