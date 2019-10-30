import math

m = float(input())

if m == 0:
    print("!=0")
    m = float(input())
else:
    print("OK")  
print("z = ",math.sqrt(m))