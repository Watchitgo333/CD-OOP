import ninja_pets
import random

owner = ninja_pets

class pet:
    def __init__(self, name, type, tricks, health = 100, energy = 100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.owner = owner.ninja("Eric", "Brusky", "Sox", "Temptations", "Tikki Cat")
        # self.owner = ninja("Eric", "Brusky", "Sox", "Temptations", "Tikki Cat")

    def sleep(self):
        print("Zzz Zzz Zzz Zzz Zzz....purrrr")
        # self.energy += 25
        while self.health < 100:
            self.health += 1
        for x in range(0, 25):
            if self.energy < 150:
                self.energy += 1
            # else: break 
        print(f"I am Feeling well rested! I'll probably see what my servant {self.owner.first_name} is up too. Maybe, I can knock stuff off the counter so he will feed me. ")
        # if(self.health == 100):
        #     self.health += 0
        # else
        print(f"{self.name}'s | Health: {self.health} | Energy: {self.energy}")
        return self

    def eat(self):
        print(f"{self.name}: 'Mlem, mlem, mlem'")
        for x in range(0, 10):
            if self.energy < 150:
                self.energy += 1
        for x in range(0, 5):
            if self.health < 150:
                self.health += 1
        print(f"{self.name}'s | Health: {self.health} | Energy: {self.energy}")
        return self

    def hide(self):
        print(f"Uh oh, you can't seem to find {self.name}!")
        print(f"Try loooking for him! Maybe shake the {self.owner.treats} box!!")
        return self

    def exercise(self, petname):
        cat_scratch = False
        if eric.pet.name == petname:
            print(f"After walking halfway around the block {self.name} frew up all over the ground and you had to carry him the rest of the way.....")
            self.energy -= 25
            self.health -= 10
        else: 
            print(f"You tried to put {self.name} in a harness and he scratched you!!")
            self.owner.cat_scratch = True
        print(f"{self.name}'s | Health: {self.health} | Energy: {self.energy}")
        print(f"{self.owner.first_name} | Cat Scratch Fever - {self.owner.cat_scratch}")
        return self

    def play(self):
        print("You notice a red dot on the wall, so you chase it!")
        self.energy -= 25
        print(f"{self.name}'s | Health: {self.health} | Energy: {self.energy}")
        return self

    def noise(self):
        sound = ["Meow", "Moww", "Hiss!"]
        random_index = random.randint(0,len(sound)-1)
        print(random.randint(0,len(sound)))
        print(sound[random_index])
        return self

class outsideCat(pet):
    def __init__(self, alias, type, abilities, feral, health=100, energy=100):
        super().__init__(alias, type, health, energy)
        self.abilities = abilities
        self.feral = feral
        self.alias = alias

sox = pet("Sox", "Cat", "Knocking stuff off the counter", 100, 100)
eric = owner.ninja("Eric", "Brusky", sox, "Temptations", "Tikki Cat")
tboy = outsideCat("T Boy","Cat", "Starting Fights through the Glass with indoor cats", True, 125, 110)

# print(__name__)
# print(locals())
# eric = ninja("Eric", "Brusky", sox, "Temptations", "Tikki Cat")

# if __name__ == "__main__":
#     print("the file is being executed directly")
# else:
#     print("The file is being executed because it is imported by another file. The file is called: ", __name__)
eric.bathe()
eric.walk()
eric.treat("Sox")
eric.feed().feed()
sox.sleep().play()
tboy.play().exercise("T Boy")

# print(eric.pet.name == "Sox")
# print()

