class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.weapon = self.Weapon(name)

    def say_name(self):
        print(f"Hero's name is {self.name}")

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

    class Weapon:
        def __init__(self, hero_name):
            self.name = f"{hero_name}'s Repulsor Blasts"
            self.damage = 500

        def use_weapon(self):
            print(f"The {self.name} deal {self.damage} damage!")

# Создаем экземпляр супер-героя
iron_man = SuperHero(
    name='Tony Stark',
    nickname='Iron Man',
    superpower='Genius-level intellect, Powered Suit of Armor',
    health_points=8000,
    catchphrase='I am Iron Man.'
)

# Используем оружие супер-героя
iron_man.weapon.use_weapon()
