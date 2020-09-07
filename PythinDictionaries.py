mydict={
    "brand":"Ford",
    "model":"Mustang",
    "year":"2016"
}#Dict-in yaradilmasi
mydict["colour"]= "red"#Dict-ə elementin elave olunmasi
print(mydict)
print(mydict)
x=mydict["model"]#model-in ekrana cixarilmasi
print(x)
mydict["year"]=2018#Dict-ə key-value-nin elave olunmasi
print(mydict)
for x in mydict:
    print(mydict)#Dict-i dovre salmaq
for x in mydict:
    print(mydict[x])#Value-lari ekrana cixarmaq
for x in mydict.values():
    print(x)#Value-lari ekrana cixarmanin diger yolu
for x in mydict.keys():
    print(x)#Keys-leri ekrana cixarmaq
for x,y in mydict.items():
    print(x,y)#Dict-in butun key-value-lari ekrana cixarmaq
if "model" in mydict:
    print("Yes,'model' is one of the keys in mydict")#Daxil edilen key-in olub olmamasini yoxlamaq
print(len(mydict))#Dict-in nece elementden ibaret oldugunu yoxlamaq
mydict["colour"]= "red"
print(mydict)#Dict-e key-value cutunu elave etmek
mydict.pop("year")
print(mydict)#year key-value-sini silmek
mydict.popitem()
print(mydict)#Sonuncu daxil edilen key-i silmek
del mydict["model"]
print(mydict)#model key-value cutunu silmek
"""del mydict
print(mydict)"""#Dict-i tamamile silmek
thisdict=mydict.copy()
print(thisdict)#Dict-i kopyalamaq
thisdict=dict(mydict)
print(thisdict)#Dict constructorundan istifade ederek dict-i kopyalamaq
my_family={
    "Father":{
        "name":"Oliver",
        "surname":"Abram",
        "age":"56"
    },
    "Child1":{
        "name":"Jacob",
        "surname":"Enfield",
        "age":"18"
    },
    "Child2":{
        "name":"William",
        "surname":"Harrington",
        "age":"21"
    },
    "Mother":{
        "name":"Ava",
        "surname":"Harrington",
        "age":"46"
    }
}
print(my_family)#nested dictionaries-in yaradilmasi


"""Father"={
        "name":"Oliver",
        "surname":"Abram",
        "age":"56"
}
"Child1"={
        "name":"Jacob",
        "surname":"Enfield",
        "age":"18"
}
"Child2"= {
    "name": "William",
    "surname": "Harrington",
    "age": "21"
}
"Mother"= {
    "name": "Ava",
    "surname": "Harrington",
    "age": "46"
}
my_family={
    "Father":Father,
    "Child1":Child1,
    "Child2":Child2,
    "Mother":Mother
}
print(my_family)"""#nested dictionaries-in yaradilmasinin diger yolu