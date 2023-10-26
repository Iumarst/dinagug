z = [int(v) for v in input("Введите числа: ").split()]
s = set()
for num in z:
    if num in s:
        print('YES')
    else:
        print('NO')
        s.add(num)