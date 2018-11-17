import math
class Test:
    def move(self, x, y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(0, 0)
    def calc_instance(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2) ** 0.5

t1 = Test()
t1.reset()
t1.move(4, 5)
t2 = Test()
t2.move(1, 1)
print(t2.calc_instance(t1))