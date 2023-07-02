import csv
import os.path

class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл поврежден"

class Item(InstantiateCSVError):
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
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

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
            return f"Длина наименования товара превышает 10 символов"
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        if not os.path.exists(os.path.join(os.path.dirname(__file__), "items.csv")):
            raise FileNotFoundError("Файл не найден")

        with open(os.path.join(os.path.dirname(__file__), "items.csv"),encoding="Windows-1251", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if "name" not in reader.fieldnames or "price" not in reader.fieldnames or "quantity" not in reader.fieldnames:
                raise InstantiateCSVError("Файл поврежден")
            for row in reader:
                name, price, quantity = row["name"], row["price"], row["quantity"]
                cls(name, float(price), int(quantity))



    @staticmethod
    def string_to_number(string_number):
        if '.' in string_number:
            return int(float(string_number))
        else:
            return int(string_number)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            return None




