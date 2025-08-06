class Animal:
    def make_sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  
        print("Dog barks!")   
        
my_dog = Dog()
my_dog.make_sound()