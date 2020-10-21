import math
min = 100.0
for a in range(1, 180):
    for b in range(1, 180):
        if a == 2 * b / 3:
            k = math.sin(math.pi * a / 180) / math.sin(math.pi * b / 180)
            if k < min:
                min = k;
            print("a = ", a, "; b = ", b, ";k = ", k)
print("min = ", min)
