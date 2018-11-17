# 클래스 은닉화, 상속

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getSpecies(self):
        return self.species
    def setSpecies(self, species):
        self.species = species
    def __str__(self):
        return "동물정보"

class Dog(Pet):
    def __init__(self, bow):
        self.bow = bow

class Cat(Pet):
    def __init__(self, yam):
        self.yam = yam
