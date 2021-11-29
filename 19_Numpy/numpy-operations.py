import numpy as np

numbers1 = np.random.randint(10,100,6)   # 10 ile 100 arasında 6 adet sayi üretsin dedik.
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 + 10        # butun elemanlara +10 ekler.
result = numbers1 - numbers2
result = numbers1 - 10        # butun elemanlara -10 ekler.
result = numbers1 * numbers2
result = numbers1 * 10
result = numbers1 / numbers2
result = numbers1 / 10

result = np.sin(numbers1)  # number1 sinus degeri alınır. 
result = np.cos(numbers1)  # number1 cosinus degeri alınır. 
result = np.sqrt(numbers1) # number1 karekok degeri alınır. 
result = np.log(numbers1)  # number1 logaritması degeri alınır. 

mnumbers1 = numbers1.reshape(2,3)  #
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
print(mnumbers2)

result = np.vstack((mnumbers1,mnumbers2)) #dikey olarak birleştirme yapar
result = np.hstack((mnumbers1,mnumbers2)) #yatay olarak birleştirme yapar

result = numbers1 >= 50 #numbers dizisini olanır ve 50 den buyuk ve esit olanlar icin True False degeri dondurur.
result = numbers1 % 2 == 0

print(numbers1[result])

print(result)