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

