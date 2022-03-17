
class ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food, cat_scratch = False):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        self.cat_scratch = cat_scratch
    
    def walk(self):
        self.pet.hide()

    def feed(self):
        print(f"Feeding {self.pet.name} {self.pet_food} wet food.")
        self.pet.eat()
        return self

    def treat(self,petname):
        print(f"You shook the {self.treats} and gave {self.pet.name} treats! Now you can walk him!")
        self.pet.exercise(petname)

    def bathe(self):
        self.pet.noise()
        print(f"Bathing {self.pet.name}")
        return self

# class pet:
#     def __init__(self, name, servant_owner, type, tricks, health = 100, energy = 100):
#         self.name = name
#         self.type = type
#         self.tricks = tricks
#         self.health = health
#         self.energy = energy
#         self.owner = ninja("Eric", "Brusky", "Sox", "Temptations", "Tikki Cat")

#     def sleep(self):
#         print("Zzz Zzz Zzz Zzz Zzz....purrrr")
#         # self.energy += 25
#         while self.health < 100:
#             self.health += 1
#         for x in range(0, 25):
#             if self.energy < 150:
#                 self.energy += 1
#             # else: break 
#         print(f"I am Feeling well rested! I'll probably see what my servant {self.owner.first_name} is up too. Maybe, I can knock stuff off the counter so he will feed me. ")
#         # if(self.health == 100):
#         #     self.health += 0
#         # else
#         print(f"{self.name}'s | Health: {self.health} | Energy: {self.energy}")
#         return self

#     def eat(self):
#         print(f"{self.name}: 'Mlem, mlem, mlem'")
#         for x in range(0, 10):
#             if self.energy < 150:
#                 self.energy += 1
#         for x in range(0, 5):
#             if self.health < 150:
#                 self.health += 1
#         print(f"{self.name}'s | Health: {self.health} | Energy: {self.energy}")
#         return self

#     def hide(self):
#         print(f"Uh oh, you can't seem to find {self.name}!")
#         print(f"Try loooking for him! Maybe shake the {self.owner.treats} box!!")
#         return self

#     def exercise(self):
#         print(f"After walking halfway around the block {self.name} frew up all over the ground and you had to carry him the rest of the way.....")
#         self.energy -= 25
#         self.health -= 10
#         print(f"{self.name}'s | Health: {self.health} | Energy: {self.energy}")
#         return self

#     def play(self):
#         print("You notice a red dot on the wall, so you chase it!")
#         self.energy -= 25
#         print(f"{self.name}'s | Health: {self.health} | Energy: {self.energy}")
#         return self

#     def noise(self):
#         print(f"Meow...... Hiss...... Mowwwwww.....")
#         return self

# sox = pet("Sox", "Cat", "Knocking stuff off the counter", 100, 100)
# eric = ninja("Eric", "Brusky", sox, "Temptations", "Tikki Cat")

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)

print(__name__)
print(locals())
# eric.bathe()
# eric.walk()
# eric.treat()
# eric.feed().feed()
# sox.sleep().play()