class Animals:
    def eat(self):
        print("хочу есть")
    color = None
    legs = 4
    sound = None

    def say(self, sound):
        print(sound, "-", sound)
    age = 0

    def birthday(self):
        self.age += 1


class Goats(Animals):
    color = "white"
    sound = "мее"

class Sheeps(Animals):
    sound = "бее"
    color = "white"

class Pigs(Animals):
    color = "pink"


class Brids(Animals):
    legs = 2


class Ducks(Brids):
    sound = "кря"
    color = "gray"

class Chicken(Brids):
    color = "yellow"

class Geese(Brids):
    sound = "га"
    color = "gray"

a = Geese()
a.birthday()
print(a.age)
a.birthday()
print(a.age)
a.birthday()
print(a.age)



