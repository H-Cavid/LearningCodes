cars=["BMW","Mersedes","Lamborghini","Ferrari","McLaren","Toyota"]
print(cars)#cars Array
print(cars[0:6])#Array-in elementlerine access
print(len(cars))#Array-in nece elementden ibaret olmasi
for x in cars:
    print(x,end=" ")#for vasitesile elementleri dovre salmaq
cars.append("Bugatti")#Append metodu vasitesile elementleri elave etmek
print(len(cars))#len metodu ile Array-in elementlerini ekrana vermek
print(cars,end=" ")
cars.pop(5)#Pop metodu vasitesile Array-dan element silmek(index-i daxil edirik)
print(cars,end=" ")
cars.remove("Mersedes")#Remove metodu vasitesile elementi Array-dan silmek
print(cars)