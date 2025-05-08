

x = True
y= False

# and
print(x and y) # False

"""#uso posible:
if (aprobo(matematicas) and aprobo(fisica)):
    print("Aprobo las dos materias")"""

# or

print(x or y) # True

""" 1 and 1 -> 1
 0 and 1 -> 0
    1 and 0 -> 0
    0 and 0 -> 0

1 or 0 -> 1
0 or 1 -> 1
0 or 0 -> 0
1 or 1 -> 1"""

print(y)

#negar y
print(not y) # True

while not y:
    print("Hola")
    break
