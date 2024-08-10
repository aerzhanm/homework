class SuperHero:
    people = 'человека'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def sey_name(self):
        print(f'my name is {self.name}')

    def duble_health(self):
        self.health_points *= 2
        return self.health_points

    def __str__(self):
        return (f'nikname: {self.nickname}, superpower: {self.superpower}/n'
                f'health_points: {self.health_points}')

    def __len__(self):
        return len(self.catchphrase)


supermen = SuperHero(
    name='Генри Кавил',
    nickname='Супермен',
    superpower='умеет летать, у него мощный удар, он неубиваемый,  а также он имеет хороший интелект',
    health_points=5000,
    catchphrase=' "Я вас всех спасу!"'

)
print(f'Этого {SuperHero.people} зовут {supermen.name}')
print(f'но все его называют {supermen.nickname}')
print(f'он очень сильный и способен на невероятные вещи, например он {supermen.superpower}')
print(f'А это его здоровье {supermen.health_points}')
print(f'а его коронная фраза это {supermen.catchphrase}')
print(f'давайте удвоим его здоровье: {supermen.duble_health()}')
print(f'давайте узнаем количество букв в его коронной фразе: {len(supermen.catchphrase)}')


class Hulk(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, super_hit, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.super_hit = super_hit
        self.fly = fly

    def duble_health(self):
        self.health_points = self.health_points ** 2
        self.fly
        return self.health_points, self.fly

    def __str__(self):
        return (f'меня зовут {self.name}, но все меня знают как {self.nickname}\n'
                f'мои суперспособности как у {supermen.nickname}а но неного слабее {self.superpower}\n'
                f' мое здоровье {self.health_points}\n'
                f'коронная фраза {self.catchphrase}')

    def fly(self):
        return f'я летаю но только хлопками'

    def phrase(self):
        return 'True in the True_phrase'


hulk = Hulk('Робеерот Брюс Беннер', 'Халк'
            , 'летать, бить, гнев', 6000, 'Не зли меня а то убью', 2000)
print(hulk)


class Villain(Hulk):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, super_hit, fly=False, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, super_hit, fly)
        self.damage = damage

    def gen_x(self):
        pass

    def crit(self):
        self.damage = self.damage ** 2
        return self.damage
