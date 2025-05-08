

lista = [1, 2, 3, 4,5]

# me pregunto, en la lista esta el valor 3
print(3 in lista) # True
print(6 in lista) # False


# not in
print(3 not in lista) # False
print(6 not in lista) # True


#el siguiente archio es de precedencia

"""2 + 2 * 3 -> primero multiplica y desp la suma
(2 + 2) * 3
2 + 2 ** 3"""


print((2 + 2 )* 3) # 8

# >> -> divide por dos cuantas veces se le indique
# 8 >> 2 # 2 -> 8/2=4, 4/2 -> 2
# 16 >> 3 # 2 -> 16/2=8, 8/2=4, 4/2=2
# 16 >> 4 # 1 -> 16/2=8, 8/2=4, 4/2=2, 2/2=1

# quiero multiplicarlo -> <<
# multiplica por dos cuantas veces se le indique
# 2 << 2 # 8 -> 2*2=4, 4*2=8
# 2 << 3 # 16 -> 2*2=4, 4*2=8, 8*2=16