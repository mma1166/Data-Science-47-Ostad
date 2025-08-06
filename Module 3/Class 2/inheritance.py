#Dad mr.object
#Mom ms.classy
#son Inno
#Daughter Multi claver

# #single inheritance
# class father:
#     def skills(self):
#         print("I can code in C++")

# class son(father):
#     pass
# inno = son()
# inno.skills()

#multi inheritance

# class mom:
#     def skills(self):
#         print("I can cook delicious Beriyani")

# class Inno(mom):
#     pass

# class Multi(mom):
#     pass
# inno = Inno()
# multi = Multi()
# inno.cooking()
# multi.cooking()

# #multi level inheritance
# class Grandpa:
#     def advice(self):
#         print("Never ignore bugs")

# class Father(Grandpa):
#     def teach (self):
#         print("Practice C++ will make youre more logical and increase thinking capability")

# class son(Father):
#     pass

# multi = son()
# multi.advice()
# multi.teach()

class Mother:
    def discipline(self):
        print("Go to bed at 10 PM")

class UncleLogic:
    def math(self):
        print("solving equations")

class Daughter(Mother, UncleLogic):
    pass

multi=Daugher()
multi.discipline()
