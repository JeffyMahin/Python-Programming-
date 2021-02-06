# Object has two characteristics/Properties:
# 1. Attribute 2. Behavior
#
# Parrot:
# name, age, color => Attribute (Class attribute and Instance attribute)
# Singing, Dancing => Behaviour


# OOP Concept: DRY- Dont Repeat Yourself(Reusable Code)


# Object is an instance
# obj = Parrot()


class Parrot:
    # class attribute
    species = 'bird'

    # instalnce attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)


# access the class attribute
print(woo.species)



# access the instance attribute

print("The parrot name is {} and age is {}".format(blu.name, blu.age))