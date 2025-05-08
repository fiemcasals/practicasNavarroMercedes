
#tabla de verdad

#0 -> Falso -> False
#1 -> Verdadero -> True

# A: en navarro llueve
# B: en mercedes llueve

#  A  |  B  |  A and B |  A or B | not A
#  0  |  0  |    0     |    0    |   1
#  0  |  1  |    0     |    1    |   1
#  1  |  0  |    0     |    1    |   0
#  1  |  1  |    1     |    1    |   0





"""False or True - > True
False and True - > False
True and True - > True
False or False - > False"""


x = True
y = False

# and
print (x and y) # False

if y and x:
    print("dio verdadero")

#uso posible
if x and y:
    print("Ambos son verdaderos")

# not
print(not False)

# en el archivo de operadores unarios solo esta lo siguiente

x = 5
y = -x

print(x) # 5
print(y) # -5

#vamos a ver el operador not
#not True -> False
#not False -> True
#not 0 -> True
#not 1 -> False

a = True
b = not a
print(a) # True
print(b) # False
