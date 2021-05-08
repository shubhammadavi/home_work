l1 = [1,2,3,4,5,6,7,8]
print(l1[0:7:3] )

l2 = ["abc", 1 , 1.5, "ghf"]
l2.append("xyz")
print(l2)

l1.append(l2)
print(l1)

l1.extend(l2)
print(l1)

l1.remove(l2)
print(l1)

l1.insert(7,l2)
print(l1)

print(l1[7][2])

del l1[7]
print(l1)

l1.clear()
print(l1)

print(l2[-3:-2])

l3=["a","b","c"]
l4=["d","e","f"]

l1=l3.copy()
print(l1)

l1=list(l4)
print(l1)

l5=l3+l4
print(l5)

l6=list((7,8,6,9,3,4))
print(l6)
