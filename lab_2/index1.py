mas = list(range(2,103))
for i in mas:
    for j in mas:
        if j != i:
            if mas[j] < mas[i]:
                mas[i] == j
                mas[j] == i
print(mas)