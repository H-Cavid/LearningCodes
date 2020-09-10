class User:
    def __init__(self,lname,fname):
        self.firstname=fname
        self.lastname=lname
    def showdata(self):
        print("My firstname is" + " " + self.firstname)
        print("My lastname is" + " " + self.lastname)
"""User1=User("Jhon","David")
User1.showdata()#Parent Class"""

"""class Student(User):
    pass
x=Student("Napaleon","Brayan")
x.showdata()#User class-indan inheritance almaq"""

"""class Student(User):
    def __init__(self,fname,lname):
        User.__init__(self,fname,lname)
x=Student("Napaleon","Brayan")
x.showdata()#User class-indaki propertyleri saxlamaq serti ile  inheritance almaq"""

"""class Student(User):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)#super methodu vasitesile parent class-in butun metodlarini kopyalamaq
                                     #(self yazilmir,cunki butun metodlari kopyaliyir
x=Student("Napaleon","Brayan")
x.showdata()"""

"""class Student(User):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.GraditionYear=2019#Child class-a property elave etmek
x=Student("Napaleon","Brayan")
x.showdata()
print(x.GraditionYear)"""

"""class Student(User):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.GraditionYear=year#Child class-a year parametrini elave etmek
x=Student("Napaleon","Brayan",2019)
x.showdata()
print(x.GraditionYear)"""

class Student(User):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.GraditionYear=year
    def Welcome(self):
        print("Welcome",self.firstname,self.lastname,"To the class of",self.GraditionYear)
x=Student("Napaleon","Hill",2019)
print(x.Welcome())#Child class-a Welcome methodunu elave etmek