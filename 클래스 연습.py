class JSS:
    def __init__(self):
        self.name = input("이름 : ")
        self.age = input("나이 : ")

    def show(self):
        print("제 이름은 {}입니다. 제 나이는 {}입니다.".format(self.name,self.age))
    
class JSS2(JSS):#클래스 계승

    def __init__(self):
        super().__init__()
        self.gender = input("성별 : ")

    def show(self):
        print("제 이름은 {}입니다.저는 {}자이고 제 나이는 {}입니다.".format(self.name,self.gender,self.age))
    
a = JSS2()
a.show()
print(a.name,a.age,a.gender)
