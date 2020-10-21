import math

def isPointAboveLine(x_a, y_a, x_b, y_b, x_c, y_c):
    v1 = [x_b - x_a, y_b - y_a]
    v2 = [x_c - x_a, y_c - y_a]
    if v1[0]*v2[1] - v2[0]*v1[1] > 0:
        return 1 #Выше отрезка
    else:
        return -1 #Ниже отрезка

def getDistanceFromPointToLine(x_a, y_a, x_b, y_b, x_c, y_c):
    v1 = [x_b - x_a, y_b - y_a]
    v2 = [x_c - x_a, y_c - y_a]
    v3 = [x_a - x_b, y_a - y_b]
    v4 = [x_c - x_b, y_c - y_b]
    if (v1[0]*v2[0] + v2[1]*v1[1] < 0) or (v3[0]*v4[0] + v3[1]*v4[1] < 0):
        if v1[0]*v2[0] + v2[1]*v1[1] < 0:
            return math.sqrt((x_a - x_c)**2 + (y_a - y_c)**2)
        else:
            return math.sqrt((x_b - x_c)**2 + (y_b - y_c)**2)
    else:
        return abs(((x_a - x_b) * (y_c - y_b) - (y_a - y_b) * (x_c - x_b)) / math.sqrt((x_a - x_b)**2 + (y_a - y_b)**2))


x_a, y_a, x_b, y_b = input().split(" ")
x_a = int(x_a)
y_a = int(y_a)
x_b = int(x_b)
y_b = int(y_b)

n, m = input().split(" ")
n = int(n)
m = int(m)

counter = 0

if x_a == x_b:
    stars_left = list()
    stars_right = list()
    for i in range(n):
        x, y = input().split(" ")
        x = int(x)
        y = int(y)
        if x < x_a:
            stars_left.append([x, y])
        else:
            stars_right.append([x, y])

    planets_left = list()
    planets_right = list()
    for i in range(m):
        x, y = input().split(" ")
        x = int(x)
        y = int(y)
        if x < x_a:
            planets_left.append([x, y])
        else:
            planets_right.append([x, y])

    for i in range(len(stars_left)):
        for j in range(len(planets_left)):
            if isPointAboveLine(stars_left[i][0], stars_left[i][1], planets_left[j][0], planets_left[j][1], x_a, y_a) * isPointAboveLine(stars_left[i][0], stars_left[i][1], planets_left[j][0], planets_left[j][1], x_b, y_b) == -1 and getDistanceFromPointToLine(x_a, y_a, x_b, y_b, stars_left[i][0], stars_left[i][1]) > getDistanceFromPointToLine(x_a, y_a, x_b, y_b, planets_left[j][0], planets_left[j][1]):
                counter +=1;
    for i in range(len(stars_right)):
        for j in range(len(planets_right)):
            if isPointAboveLine(stars_right[i][0], stars_right[i][1], planets_right[j][0], planets_right[j][1], x_a, y_a) * isPointAboveLine(stars_right[i][0], stars_right[i][1], planets_right[j][0], planets_right[j][1], x_b, y_b) == -1 and getDistanceFromPointToLine(x_a, y_a, x_b, y_b, stars_right[i][0], stars_right[i][1]) > getDistanceFromPointToLine(x_a, y_a, x_b, y_b, planets_right[j][0], planets_right[j][1]):
                counter +=1;

else:
    stars_up = list()
    stars_down = list()
    for i in range(n):
        x, y = input().split(" ")
        x = int(x)
        y = int(y)
        if isPointAboveLine(x_a, y_a, x_b, y_b, x, y) == 1:
            stars_up.append([x, y])
        else:
            stars_down.append([x, y])

    planets_up = list()
    planets_down = list()
    for i in range(m):
        x, y = input().split(" ")
        x = int(x)
        y = int(y)
        if isPointAboveLine(x_a, y_a, x_b, y_b, x, y) == 1:
            planets_up.append([x, y])
        else:
            planets_down.append([x, y])


    for i in range(len(stars_up)):
        for j in range(len(planets_up)):
            if isPointAboveLine(stars_up[i][0], stars_up[i][1], planets_up[j][0], planets_up[j][1], x_a, y_a) * isPointAboveLine(stars_up[i][0], stars_up[i][1], planets_up[j][0], planets_up[j][1], x_b, y_b) == -1 and getDistanceFromPointToLine(x_a, y_a, x_b, y_b, stars_up[i][0], stars_up[i][1]) > getDistanceFromPointToLine(x_a, y_a, x_b, y_b, planets_up[j][0], planets_up[j][1]):
                counter +=1;
    for i in range(len(stars_down)):
        for j in range(len(planets_down)):
            if isPointAboveLine(stars_down[i][0], stars_down[i][1], planets_down[j][0], planets_down[j][1], x_a, y_a) * isPointAboveLine(stars_down[i][0], stars_down[i][1], planets_down[j][0], planets_down[j][1], x_b, y_b) == -1 and getDistanceFromPointToLine(x_a, y_a, x_b, y_b, stars_down[i][0], stars_down[i][1]) > getDistanceFromPointToLine(x_a, y_a, x_b, y_b, planets_down[j][0], planets_down[j][1]):
                counter +=1;
print (counter)
