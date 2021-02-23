#key - value
# 34 => istanbul

#sehirler = ['İstanbul','Ankara']
#plakalar = [34 , 6]

#print(sehirler[plakalar.index(34)])

# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34

# plakalar = { 'kocaeli' : 41, 'istanbul': 34 }

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'

# print(plakalar)

users = {
    'ebubekirdgn': {
        'age': 27,        
        'roles': ['user'],
        'email': 'dgn@gmail.com',
        'address': 'samsun',
        'phone': '1231321'
    },
    'aliveli': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'veli@gmail.com',
        'address': 'istanbul',
        'phone': '1231321'
    }
}

print(users['ebubekirdgn']['roles'][0])
print(users['ebubekirdgn'])
print(users['aliveli']['roles'][0])



