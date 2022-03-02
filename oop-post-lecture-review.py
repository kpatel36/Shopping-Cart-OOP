# object oriented programming aka OOP
# basis of oop is an object
# objects have characteristics:
# attributes and behaviors
# DRY = don't repeat yourself - create multiple different objects that have similar attributes and behaviors but are actually different

# example of an object:
# cat would be an object, a cat can have the following properties:
    # name, age, color, weight, breed --> attributes that object can have (describing what the object is like)
    # talk, sing, play, eat, jump -> behaviors that object will have (what actions the object can do)

#basic Principles:
    # object
    # classes
    # methods
    # inheritence 

# objects 
    # objects = instance
    # object is instantiation of a class
    # object is an instant we made from a particular class
    # an instant is a specific object from a particular class
        # ex - can have multiple instants/cats from same class of cat
        
# classes:
    # blueprint for an object yo want to create
    # class is a sketch of our cat object, with labels
    # labels will contain attributes and behaviors (everything that will describe whatever object we have)
    # when a class is defined, it's only the description of whatever object you want to make. the object itself is not actually defined yet
    # # in order to define (or make) our object, that will be where we instantiate our class
    # Class Syntax:
class Cat():
    # attributes: name, age, color, weight, species
    # main way to assign attributes is via init method
    # init is the initiallizer method that is run as soon we create any sort of object within that class
    #class attribute (these should stay the same no matter how many instances we create) (i.e. species of cat)
    species = "cat"
    # the self just refers 
    # instance attributes - (these change with each instance of the class) vs 
    def __init__ (self, name, age, color, weight): #--> include attributes that will change for each object/instant
        self.name = name 
        self.age = age
        self.color = color
        self.weight = weight

    # making methods for our behaviors
    # behaviors: "alking and singing
    def talking(self): #ALWAYS NEED TO ADD PARAMETER SELF to make sure our methods are accessed by the objects
        print (f"{self.name} is now talking to itself in the corner")
    
    def singing(self, song):
        print( f"{self.name} can sing the song {song}")

cat1 = Cat("Hecate", 5, "Black", "30lbs")
cat2 = Cat("Tate", 2, "orange", "80lbs")

# accessing class attributes
print (f"This animal class is based on the {cat1.__class__.species} species") # {cat1.__class__.species}  = from object of class , pull this attribute

# accessing instance attributes - {objectname.attributename}
print(f"{cat1.name} is {cat1.age} years old and weighs {cat1.weight}.")
print(f"{cat2.name} is {cat2.age} years old and weighs {cat2.weight}.")

# calling instance methods:
cat1.talking()
cat2.singing("Happy Birthday")

# Inheritence
# a way of creating a new class using details of existing class without modifying that original existing
# new class is a derived class aka child class
# old class is a base class aka parent class
# we want to make a class of Maine Coon,

class MaineCoon(Cat): #parameter Cat because it is inheriting it from parent class Cat
    def __init__(self):
        # super init line allows us to run the init method of the parent class
        super().__init__("cat", 3, "orange", "50lbs")

    def talking(self): #ALWAYS NEED TO ADD PARAMETER SELF to make sure our methods are accessed by the objects
        print (f"{self.name} is now talking to its parent")
    
    def singing(self, song):
        print( f"{self.name} can sing the song {song}")

    def sleeping (self):
        print (f'{self.name} is currently sleeping.')


garfield = MaineCoon() 
garfield.talking()
garfield.sleeping()
garfield.singing("Twinkle Twinkle Little Star")



#OOP SHOPPING CART:
# object --> cart (lists or dictionaries)
# what attribute and behaviors does it need ?
# attributes --> items in the cart, price, quantity
# behaviors --> add items, remove items, see the item, clear the cart, quit
# oop allows you to repeat same element for multiple instances or users
# each instance could be a new user
# each object - even if its in the same class - it doesn't translate into another class