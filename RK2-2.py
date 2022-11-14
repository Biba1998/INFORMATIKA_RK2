with open("stdin.txt") as f:
    list = []
    for i in f:
        list.append(int (i))
    PERIMETR = list[0] + list[1] + list[2]
    POLUPERIMETR = float(PERIMETR) / 2
    PLOCHAD = (POLUPERIMETR * (POLUPERIMETR - list[0]) * (POLUPERIMETR - list[1]) * (POLUPERIMETR - list[2]))**0.5
with open("stdout.txt", "w") as f:
    f.write(str(PERIMETR) + '\n')
    f.write(str(PLOCHAD) + '\n')
    if (list[0]==list[1]==list[2]):
        f.write('Treugolnik pravelno')
