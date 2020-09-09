#Example number 1:
class Myclass:
    x=5
p1=Myclass()
print(p1.x)#CLass teyin etmeyin sade varianti
#Example number 2:
class Person:
        def __init__(mysillyobject,name,age):#isare etmek ucun istenilen adi qoymaq olar,self olmasi mecbur deyil
            mysillyobject.name=name
            mysillyobject.age=age
        def MyFunc(silly):
            print("Hello,My name is" + " " + silly.name)
p1=Person("Jhon",36)
p1.age=18
print(p1.age)

