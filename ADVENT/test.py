import math

def getIntegerPlaces(theNumber):
    if theNumber <= 999999999999997:
        return int(math.log10(theNumber)) + 1
    else:
        return len(str(theNumber))

i = 12345678
j = pow(10, int(getIntegerPlaces(i)/2))

print(i // j)
print()
print(i)
print(j)

g = ["h"]

h = ["." for _ in range(3)]
print(h)


if 4 % 2:
    print("hi")
