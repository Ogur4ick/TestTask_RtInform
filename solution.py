mass = []
lenn = int(input())
for i in range(lenn):
    mass.append(int(input()))
print(mass)

result = dict()
for i in mass:
    result[i] = mass.count(i)
print(result)

    
