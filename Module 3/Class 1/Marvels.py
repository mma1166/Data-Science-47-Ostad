# #class
# class Avenger:
#     def fight(self):
#         print("Avangers, Start Fighting !!!")

# #Object
# ironman = Avenger()
# hulk = Avenger()

# ironman.fight()
# hulk.fight()

# #Introducing Method

# #class
# class Avenger:
#     def introduce(self,name):
#         print(f"I am {name} and I protect the world!")

# #Object
# ironman = Avenger()

# thor=Avenger()
# ironman.introduce("Tony Stark")
# thor.introduce("Thor")

# #Default Constructor
# class Avanger:
#     def __init__(self):
#         print("A New Avanger has joined the team.")

# captain = Avanger()


# class Avanger:
#     def __init__(self,name,power):
#         self.name=name
#         self.power=power

#     def show(self):
#         print(f'{self.name}has power {self.power}')

#     def fight(self):
#         print(F'{self.name} start fighting')


# spiderman = Avanger("Spider-man", "web-slinging")

# spiderman.show()
# spiderman.fight()

class Hero:
    def protect(self):
        print("protecting the world")

class Ironman(Hero):
    def Fly (self):
        print("Flying in the suit")

tony = Ironman()
tony.protect()