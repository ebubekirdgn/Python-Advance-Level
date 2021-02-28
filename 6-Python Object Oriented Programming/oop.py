import datetime

# Object Oriented Programming (OOP)

# class => Person (name, surname, birthday, calculateAge())
# instance (object)

lst1 = [1,2,3]
lst2 = [1,2,3,4]


result = type(lst1) # ekranda : <class 'list'> yazar
result = type(lst2) # ekranda : <class 'list'> yazar


#bugün kodu :
bugun = datetime.date.today()
#bugün format :
bugun_format = bugun.year


print(bugun_format)

print(result)
