class Pet:
    def __init__(self, pet_info):
        self.name = pet_info["name"]
        self.type = pet_info['type']
        self.tricks = pet_info['tricks']
        self.energy = 100
        self.health = 100
        self.sound = pet_info['sound']

    def sleep(self):
        print(f"{self.name} is now sleeping. They look so cute!")
        self.energy += 25
        if self.energy > 100: self.energy = 100
        print(f"{self.name} now has {self.energy} energy")
    
    def eat(self):
        print(f"{self.name} is eating their food... Yummy yums!")
        self.energy += 5
        if self.energy > 100: self.energy = 100
        self.health += 10
        if self.health > 100: self.health = 100
        print(f"{self.name} now has {self.energy} energy and {self.health} health")

    def play(self):
        print(f"{self.name} is playing with their toys <3 <3 <3")
        self.health += 5
        if self.health > 100: self.health = 100
        print(f"Somehow that increases {self.name}'s health to {self.health}")

    def noise(self):
        print(f"{self.name}: {self.sound}")

class Cat(Pet):
    def __init__(self, pet_info):
        super().__init__(pet_info)
        self.lives = 9

    def noise(self):
        print('Meeeeeoooooow')

    def sleep(self):
        print("Time for a cat nap!")
        super().sleep()