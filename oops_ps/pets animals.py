class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow")
    

d=dog()

d.bark()