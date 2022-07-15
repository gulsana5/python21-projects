from models import Cars
from models import User
from models import Category, Product, Comment
from .serializers import ProductSerializer, CategorySerializer


# round()

def auto_greate():
    marka = input("Марк: ")
    model = input("Модель: ")
    year = int(input("Год выпуска:"))
    engine = round(float(input("Объем двигателя:")), 2)
    color = input("Цвет: ")
    body = input(f"Тип кузова {Cars.bodytip}: ")
    mileage = int(input("Пробег: "))
    price = round(float(input("Цена: ")), 3)

    obj = Cars(marka, model, year, engine, color, body, mileage, price)

    cat_title = input(f"Выберите категорию {[cat.title for cat in Cars.objects]}:")

    print("Выберите категорию:")
    for cat in Cars.objects:
        print(cat.title)
    cat_title = input("=====================\n")
    category = (Cars, "title", cat_title)

    Cars(marka, model, year, engine, color, body, mileage, price)
    return "Успешно создан"

def auto_detail(p_id):
    product = Cars(Product, "id", int(p_id))
    serializer = ProductSerializer()
    return serializer.serialize_obj(product)

def auto_delete(p_id):
    product = Cars(Product, "id", int(p_id))
    Product.objects.remove(product)
    return "Успешно удален"

def auto_update(p_id):
    product = Cars(Product, "id", int(p_id))
    field = input("Введите поле для изменения: ")
    if field in dir(Cars):
        print(f"old value: {getattr(product, field)}")
        value = input(f"{field} = ")
        setattr(product, field, value)
    else:
        raise Exception(f"Поля {field} нет в продукте")
    return auto_detail(p_id)

def category_create():
    title = input("Введите название категории: ")
    Category(title)
    return "Категория была успешно создана"

def create_comment():
    email = input("Введите email: ")
    user = Cars(User, "email", email)
    print("Выберите авто:")
    for p in Product.objects:
        print(p.title)
    title = input("=======================\n")
    product = Cars(product, "title", title)
    body = input("Введите комментарий: ")
    Comment(user, product, body)
    return "Комментарий успешно добавлен"

u = User("admin", "admin", "k")
u.register("12345678", "12345678")
u.login("12345678")
cat = Category("test")
p = Product("hello", 345, "vghjk", 2, cat)
Comment(u, p, "hello world")