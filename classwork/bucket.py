# для класса выделяют :
#  методы - это функции внури класса
#  атрибуты - переменные внутри класса

class Cell:
    '''ячейка'''
    content = 1
    content_type = int()
    def set_value(val):
        content = val
        content_type = type(val)
# СОЗДАЕМ ЭКЗЕМПЛЯР ОБЬЕКТА КЛАССА
# экземпляр (instance)
a1 = Cell()
b1 = Cell()

print(a1.content_type)

print(
    'имена класса  Cell:', Cell().__dict__,
    'имена ячейка ф1:', a1.__dict__,
    'имена ячейка b1:', b1.__dict__,
    sep = '\n')

a1.content = 100




# здесь создадим класс хранилища

class Bucket:
    '''Хранилище объектов для статического сайта'''

    def add(self, obj):
        '''Поместить объект в бакет'''
        self.content = obj
        print('Добавлен',  obj)
        

website = Bucket()
website.add(obj='index.html')  # вызов метода
Bucket.add(self=website, obj='index.html')  # на самом деле происходит вот это

print(website.content)
# 
# 
# 
# 
class Bucket:
    '''Хранилище объектов для статического сайта'''

    def __init__(self):
        self.content = []

    def add(self, obj):
        '''Поместить объект в бакет'''
        self.content.append(obj)
        print('Добавлен',  obj)

    def inspect(self):
        '''Проверить содержимое'''
        print('Текущее содержимое бакета:')
        for item in self.content:
            print('     ', item)


website = Bucket()

website.add('index.html')  # вызов метода
website.add('main.css')
website.inspect()


# самосвал

# Самосвал

class Truck:
    '''Самосвал загружает в ковш и выгружает из него в другом месте'''

    def __init__(self, *args: tuple) -> None:
        print('Загружено в ковш:')
        self._args = args
        [print(i) for i in args]

    def __len__(self):
        return len(self._args)

    def __eq__(self, other: object) -> bool:
        return (isinstance(other, type(self)) 
                and self._args 
                    == other._args)

    def __hash__(self) -> int:
        return hash(self._args)

    def __del__(self):
        print('Содержимое выгружено из ковша!')



transport1 = Truck('песок', 'щебень', 'земля', 'блоки')
transport2 = Truck('песок', 'щебень', 'земля', 'блоки')

# Проверка на вхождение объекта
hash_d = {transport1: 1, transport2: 3}
print(hash_d) #  хэш один и тот же!

# если закомментировать функцию eq,
# то хэш нового экземпляра будет всегда разный


# Соединение с БД

class Connection:
    '''Соединение с базой данных'''

    def __init__(self, ip):
        self.host = ip
        print('Соединение с:', self.host)

    def send_query(self, query):
        print(f'Запрос {query} отправлен')

    def __del__(self):
        self.host = None
        print('Соединение разорвано!')

conn = Connection('127.0.0.1')
conn.send_query('SELECT * FROM table;')


class Bucket:
    '''Хранилище объектов для статического сайта'''

    def __init__(self):
        self.content = []

    def get_var_name(self):
        for key, val in globals().items():
            if val is self:
                return key

    def __str__(self):
        return f'Содержимое {self.get_var_name()}: ' + ', '.join(self.content)

    def __bool__(self):
        return self.content != []

    def add(self, obj):
        '''Поместить объект в бакет'''
        self.content.append(obj)
        print('Добавлен',  obj)

    def inspect(self):
        '''Проверить содержимое'''
        print('Текущее содержимое бакета:')
        for item in self.content:
            print('     ', item)


website = Bucket()

print(bool(website))

website.add('index.html')  # вызов метода
website.add('main.css')

print(website)
print(bool(website))




# Строки

class Row:
    
    def __init__(self, *args):
        self._args = args

    def __eq__(self, other: object) -> bool:
        return self._args == other._args

    def __add__(self, other):
        return self._args + other._args if isinstance(other, Row) else self._args + other

r1 = Row(1, 2, 3)
r2 = Row(1, 2, 3)

print(r1 + r2)
print(r1 + (1, 2, 3))



# Имитация вызова функции

# Функция создается следующим образом
def foo(*args, **kwargs):
    print(args, kwargs)

# Можно создать функцию самостоятельно
class Foo:
    
    def __call__(self, *args: tuple, **kwargs: dict) -> any:
        print(args, kwargs)

foo = Foo()

foo(1, 2, 3, a=4, b=5)



