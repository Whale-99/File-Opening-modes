# Класс для продуктов
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # Возвращаем строку в формате: "<название>, <вес>, <категория>"
        return f"{self.name}, {self.weight}, {self.category}"

# Класс для магазина
class Shop:
    __file_name = 'products.txt'  # Приватное свойство с именем файла для хранения продуктов

    def get_products(self):
        # Чтение всех продуктов из файла и возврат единой строки с ними
        try:
            with open(self.__file_name, 'r') as file:
                # Читаем все строки и удаляем лишние пробелы
                return file.read().strip()
        except FileNotFoundError:
            return ""  # Если файла ещё нет, возвращаем пустую строку

    def add(self, *products):
        # Получаем уже существующие продукты для проверки дубликатов
        existing_products = self.get_products().splitlines()
        existing_names = {line.split(',')[0].strip() for line in existing_products}

        # Открываем файл для добавления новых продуктов
        with open(self.__file_name, 'a') as file:
            for product in products:
                # Проверяем, если продукт уже есть по названию
                if product.name in existing_names:
                    print(f"Продукт {product} уже есть в магазине")
                else:
                    # Добавляем новый продукт в файл и в список существующих имен
                    file.write(str(product) + '\n')
                    existing_names.add(product.name)  # Обновляем список имен

# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Использование __str__ метода для печати информации о продукте

s1.add(p1, p2, p3)  # Добавляем продукты в магазин

# Выводим все продукты, которые есть в магазине
print(s1.get_products())
