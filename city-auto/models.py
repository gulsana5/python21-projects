
class Category:
    objects = []

    def __init__(self, title):
        self.title = title
        Category.objects.append(self)
    
    def __str__(self):
        return self.title
    
class Cars:
    objects = []
    _id = 0
    bodytip = ("sedan", "miniven", "picap", "universal", "kype")

    def __init__(self, marka, model, year, engine, color, body, mileage, price):
        self.marka = marka
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.body = body
        self.mileage = mileage
        self.price = price
    
    def get_info(self):
        return '\n'.join((f"Марка: {self.marka}",
    f"Модель: {self.model}",
    f"Год выпуска: {self.year}",
    f"Объем двигателя: {self.engine}",
    f"Цвет: {self.color}",
    f"Тип кузова: {self.body}",
    f"Пробег: {self.mileage}",
    f"Цена: {self.price}"))

Solaris = Cars('Kia','K7', 2.0, 2022, 'white', 'sedan', 0.0, 10000.0)

print(Solaris.get_info())


