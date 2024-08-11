# Принципы ООП, GIT clone
# Наследование полиморфизм инкапсуляция Абстракция
# DRY- НЕ повторяйся
# супер класс \ родительский класс
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def reads(self):
        print('я читаю книгу под авторством:', self.author)
    def __str__(self):
        return (f'название:{self.title}\n'
                f'автор:{self.author}\n'
                f'цена:{self.price}\n')



tamirlan = Book('блич', 'Тамирлан', 2500)
print(tamirlan)
tamirlan.reads()


# print(tamirlan)
# tamirlan.reads()


# Дочерний класс
class Nowella(Book):
    def __init__(self, title, author, price, pnj):
        super().__init__(title, author,price)
        super().__init__(title, author, price)
        Book.__init__(self, title, author, price)
        self.pnj = pnj


    def __str__(self):

        return (f'{super().__str__()}'
                f'{self.pnj}')


    def reads(self):
        print('я читаю книгу под авторством:', self.author, 'и я купил ее за', self.price)


dan = Nowella('наруто', 'Дэн', 2000,'70x20')
dan.reads()
print(dan)
dan = Nowella('наруто', 'Дэн', 2000, '70x20')


# dan.reads()
# print(dan)
class Reads:
    def __init__(self, name):
        self.name = name

    def reads(self):
        print(f'я {self.name} читаю манги')

class Manga: ...
    #def anime(self):
       # print(f'я {self.name} смотрю аниме')


class Anime: ...
beka = Reads('beka')
# beka.reads()
# beka.anime()