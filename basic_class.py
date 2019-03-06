
# parent class
class Organism:
    # class attributes
    name = "Unknown"
    species = "Unknown"
    legs = None # None is a special data type
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    # method belong to this class
    def information(self): # self: access to the 'Organism' class
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg # return to the main calling this method 'information'

# child class instance
class Human(Organism): # inherit from Organism
    # override with its own custom attribute
    name = 'MacGuyver'
    species = 'Homesapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

# another child class instance
class Dog(Organism):
    name = "Spot"
    species = 'Canine'
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = 'Earth'

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg

# another child class instance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dns = "Sequence C"
    origin = 'Mars'

    def replication(self):
        msg = "\nTHe cells begin to divide and multiply into two separate organism!"
        return msg


if __name__ == "__main__":
    
    human = Human() # instantiate
    print(human.information()) # inherit
    print(human.ingenuity()) # override with child class

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())