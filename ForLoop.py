mylist=["BMW","Mersedes","Bentley"]
for x in mylist:
    print(x,end=" ")#listin elementlerini capa verir

for x in "carsname":
    print(x,end=" ")#String-in elementlerini capa verir

thislist=["Kia","Toyota","Hundai","Ford"]
for x in thislist:
    print(x,end=" ")
    if x =="Toyota":
        break#Toyota-ya gelende Toyotani ekrana vermek serti ile dongunu saxliyir

thislist=["Kia","Toyota","Hundai","Ford"]
for x in thislist:
    if x =="Toyota":
        break
    print(x, end=" ")#Toyota-ni goren kimi dongunu saxliyir,Toyota-ni ekrana vermir

thislist=["Kia","Toyota","Hundai","Ford"]
for x in thislist:
    if x =="Toyota":
        continue
    print(x, end=" ")#Toyata-ni gormezden gelir


for x in range(6):
    print(x,end=" ")#0-dan 6-ya kimi ededleri ekrana cixarir
for x in range(2,20,3):
    print(x,end=" ")#2-den 20-e qeder ededleri 3-3 ekrana cixarir
for x in range(3-15):
    print(x,end=" ")
else:
    print("Finally finished")#Kodun bitdiyini gosterir


mylist=["BMW","Mersedes","Bentley"]
thislist=["Kia","Toyota","Hundai","Ford"]
for x in mylist:
    for y in thislist:
        print(x,y,end=" ")#Nested loops mylistdeki her birini digerinin hamsinda yoxluyur

for x in [1,2,3,4,5,6]:
    pass#funksiyaya hecne yazmiyib error almamaq ucun istifade olunur pass sozu
