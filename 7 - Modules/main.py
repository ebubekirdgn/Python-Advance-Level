import mod

# result = help(mod) mod hakkında bize genel bilgi verir.
# result = help(mod.func) modun icindeki fonksiyon hakkında bize bilgi verir
result = mod.number
result = mod.numbers
result = mod.person["name"]
print(result)
result = mod.person["city"]
result = mod.func(10)

p = mod.Person()
p.speak()

print(result)