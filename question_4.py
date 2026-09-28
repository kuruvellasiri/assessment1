#polymorphism
"""base class"""
class Animal:
    def make_sound(self):
        pass
"""represents a dog """
class dog(Animal):
    def  make_sound(self):
        print("woof!")
"""represents a cat """
class cat(Animal):
    def make_sound(self):
        print("moew!")

doggy=dog()
Cat=cat()

doggy.make_sound()
Cat.make_sound()
