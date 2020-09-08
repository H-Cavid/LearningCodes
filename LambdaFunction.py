def my_function():
    print("Hello World")
my_function()#adi void  funksiyanin yazilma qaydasi
#Example number 1:
def funtion(a):
    return a+10
print(funtion(5))#adi funksiya yazilisi

x= lambda a:a+10
print(x(5))#Lambda funksiyasi ile yazilis
#Example number 2:
def somefunction(a,b):
    return a*b
print(somefunction(5,6))#adi return funksiyasi

x= lambda a,b: a*b
print(x(5,6))#Lambda funksiyasi ile yazilis

#Example number 3:
def anyfunction(a,b,c):
    return a+b+c
print(anyfunction(5,6,2))#adi funksiya yazilisi

x=lambda a,b,c:a+b+c
print(x(5,6,2))

#Example number 4:
def thisfunction(x):
    return x*2
print(thisfunction(11))#Adi funksiyanin yazilisi

def thosefunction(n):
    return  lambda x:x*n
result=thosefunction(2)
print(result(11))#Lambda funksiya ile yazilis

#Example number 5:
def those_function(n):
    return x*n
conculision=thosefunction(3)
print(conculision(11))#Adi funksiyali variant

def that_function(n):
    return  lambda x:x*n
consequence=that_function(11)
print(consequence(3))#Lambda funksiya ile yazilis

#Example number 6:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))#Lambda funksiyasi ile yazilis
