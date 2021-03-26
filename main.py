import numpy as np

print('Zadanie 1')
liczby = np.arange(3, 3 * 16, 3)
print(liczby)

print('Zadanie 2')
a = np.array([0.8, 2.55, 5.29, 7.44, 9.73])
print(a)
print(a.dtype)
b = a.astype('int64')
print(b)
print(b.dtype)

print('Zadanie 3')


def tab(x):
    t = np.arange(1, x * x + 1).reshape((x, x))
    print(t)


n = int(input('Podaj liczbę n: '))
print(n)
tab(n)

print('Zadanie 4')


def ciag(x, y):
    y = np.logspace(1, y, num=y, base=x)
    print(y)


a = int(input('Podaj pierwszą liczbę: '))
print(a)
b = int(input('Podaj ilość liczb ciągu: '))
print(b)
ciag(a, b)

print('Zadanie 5')
a = int(input('Podaj wartość wektora: '))
print(a)


def wek(x):
    mat_diag = np.diag([x - 1 - i for i in range(x)])
    print(mat_diag)


wek(a)

print('Zadanie 6')
slowo = 'okno'
s = np.array(list(slowo))
s1 = np.diag(s[::-1])
s1[0] = s
s1[:, 0] = s
print(s1)
