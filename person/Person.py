class Person:
    def __init__(self, *args):
#    def __init__(self, name, age, address):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
    def greeting(self):
        print("안녕하세요. 저는 {0}이고, {1}살이며, {2}에 삽니다.".format(self.name, self.age, self.address))

        


