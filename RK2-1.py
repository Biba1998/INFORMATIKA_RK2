FIRST = int(input())
SECOND = int(input())
TRI = int(input())
PERIMETR = FIRST + SECOND + TRI
POLUPERIMETR = float(PERIMETR) / 2
PLOCHAD = (POLUPERIMETR * (POLUPERIMETR - FIRST) * (POLUPERIMETR - SECOND) * (POLUPERIMETR - TRI))**0.5
print('Периметр =', PERIMETR)
print('Площадь =',PLOCHAD)
if (FIRST==SECOND==TRI):
    print('Треугольник правильный')
    

