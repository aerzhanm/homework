class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price





    def reads(self):
        print (f'Я читаю книгу под авторством:', self.author)


    def __str__(self):
        return (f'название: {self.title}\n'
                f'автор: {self.author}\n'
                f'цeна: {self.price}\n')
erzhan = Book('Мастер и Маргарита', 'Михаил Булгаков', 550, )
print(erzhan)
erzhan.reads()

class Nowella(Book):

    def __init__(self, title, author, price, pnj):
        super().__init__(title, author, price)
        #Book.__init__(self, title, author, price)
        self.pnj = pnj

    def reads(self):
        print(f'я купил книгу под авторством {self.author}а за {self.price}')

    def __str__(self):
        return (f'{super().__str__()}'
                f'{self.pnj}')

musi=Nowella('три друга','Ремарк', 2000,'70x20' )

musi.reads()
print(musi)




