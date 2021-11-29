import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]   
result = numbers[-1]   # 75 degeri
result = numbers[0:3]  # 0,5,10
result = numbers[:3]   # 0,5,10
result = numbers[3:]   # 15 den sona kadar gider
result = numbers[::]   # butun listeyi verir
result = numbers[::-1] # sagdan sola dogru verir listeyi tersine cevirir.

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]]) # 3x3 lük ;matris verir bize
result = numbers2[0]        # [0,5,10]  
result = numbers2[2]        # [50,75,85]
result = numbers2[0,2]      # 10 
result = numbers2[2,1]      # 75
result = numbers2[:,2]      # 10,25,85
result = numbers2[:,0]      # 0,15,50
result = numbers2[:,0:2]    # [0,5],[15,20],[50,75] 2 dahil olmayacak
result = numbers2[-1,:]     # [50,75,85] son satirdaki tüm elemanları getir dedik.
result = numbers2[:2,:2]    # [0,5],[15,20] verir.

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 # referans
arr2 = arr1.copy()

arr2[0] = 20

print(arr1)
print(arr2)



