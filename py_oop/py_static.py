# 파이썬 메소드 선언
# 클래스 밖에 있으면 함수

class MyStatic:
    def __init__(self):
        self.__x = 0
        self.__y = 0
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y


a = MyStatic()
print(MyStatic.getX(a))              # 클래스 메소드로 사용
print("a값 : ", a.getX())            # 인스턴스 메소드로 사용
print("b값 : ", a.getY())
