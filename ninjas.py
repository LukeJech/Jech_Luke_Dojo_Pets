import pets

class Ninja:
    def __init__(self, ninja_info):
        self.first_name = ninja_info["first_name"]
        self.last_name = ninja_info["last_name"]
        self.treats = ninja_info["treats"]
        self.pet_food = ninja_info["pet_food"]
        self.pet = pets.Pet(ninja_info["pets"]["reggie"])
        self.cat = pets.Cat(ninja_info["pets"]['kitty'])
    
    def feed(self):
        print(f"{self.first_name} puts some {self.pet_food} in a bowl for {self.pet.name}")
        self.pet.eat()

    def walk(self):
        print(f"{self.first_name} takes {self.pet.name} for a nice walk outside.")
        self.pet.play()

    def bathe(self):
        print(f"{self.first_name} starts to give {self.pet.name} a bath.")
        self.pet.noise()
        self.pet.noise()
        self.pet.noise()
        print(f"Apparently {self.pet.name} hates the bath...")
#     # implement __init__( first_name , last_name , treats , pet_food , pet )
    
#     # implement the following methods:

#     # bathe() - cleans the ninja's pet invoking the pet noise() method
