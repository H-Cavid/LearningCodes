#LEGB--->>>Local,Enclosing,Global,Built-in
x=6#Global Scope-->>Hər yerde istifade etmek mumkundu,globaldadi.
def foo():
    x=67#Enclosing Scope-->>Nested function-lar teyin olunub,icra prosesi birinci bar,sonra foo,sonra ise global Scope-dur.
    print(x)
    def bar():
        x=89#local Scope-->>Funksiyanin icinde teyin olunduguna gore,colde istifade etmek mumkun deyil
        print(x)
    bar()
print(x)
foo()

x=6
def foo():
    x=67
    print(x)
    def bar():
        #x=89
        print(x)
    bar()
print(x)
foo()
"""Local Scope-da deyisen olmadigi ucun Enclosingdekini gotrur,yeniden bari cagirdiqda ise yeniden Enclosinge baxir"""
x=6
def foo():
    #x=67
    print(x)
    def bar():
        #x=89
        print(x)
    bar()
print(x)
foo()
"""Ne Local Scope-da,Ne de Enclousing Scooe-da x olmadigi ucun GLobal Scope-dan x goturur.  """
import math

def foo():
    #x=67
    #math.pi=45
    print(math.pi)
    def bar():
        #x=89
        print(x)
    bar()
print(x)
foo()
""" Hec yerde x olmadigi ucun built in olaraq ozu verir deyer"""