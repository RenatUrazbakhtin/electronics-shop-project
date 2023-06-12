import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        if len(new_name) > 10:
            print("Длина наименования товара превышает 10 символов")
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        with open(os.path.join(os.path.dirname(__file__), "items.csv"), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, price, quantity = row["name"], row["price"], row["quantity"]
                cls(name, float(price), int(quantity))



    def string_to_number(self, string):
        if '.' in string:
            return int(float(string))
        else:
            return int(string)


