class Lexsus:
    marka = 'машина'

    def __init__(self, name, nickname, color, speed, time_b_100, stoimost):
        self.name = name
        self.nickname = nickname
        self.color = color
        self.speed = speed
        self.time_b_100 = time_b_100
        self.stoimost = stoimost

    #def __str__(self):
       # return f'name: {self.name},{self.color},{self.speed},{self.time_b_100},{self.stoimost}'

    def duble_speed(self):
        self.speed *= 2
        return self.speed


mersedes = Lexsus(
    name='Mersedes M5',
    nickname='black pantera',
    color='black, blue, red',
    speed=320,
    time_b_100=2.8,
    stoimost="23 000 dollarov"
)


print(f'name: {mersedes.name}')
print(f'nickname: {mersedes.nickname}')
print(f'{mersedes.color}')
print(mersedes.speed)
print(mersedes.time_b_100)
print(mersedes.stoimost)
print(mersedes.duble_speed())
