# 1 задание

name = input('Введите Ваше имя: ')
age = int(input('Ваш возраст: '))

print("Привет", name, ", тебе ", age, " лет!")

birthday = str(input("Когда у Вас день Рождения?: "))
fav_num = int(input("Введите Ваше любимое число: "))

print("Вы родились:", birthday, ", Ваше любимое число: ", fav_num, " и это здорово!")

# 2 задание

time = int(input("Введите произвольное количество секунд: "))
t = time

minutes = (t // 60) % 60
m = minutes

hours = t // 3600
h = hours

seconds = (t % 3600) % 60
s = seconds

print("{:02}:{:02}:{:02}".format(h, m, s,))

# 3 задание

n = int(input("Введите число: "))

xx = (str(n) + str(n))
xxx = (str(n) + str(n) + str(n))

x = (n + int(xx) + int(xxx))

# print(n)
# print(xx)
# print(xxx)

print(x)

# 4 задание

n = int(input("Введите целое положительное число: "))
max_n = n % 10
n = n // 10
while n > 0:
    if n % 10 > max_n:
        max_n = n % 10
    n = n // 10
print(max_n)

# 5 задание

x = int(input("Введите выручку: "))
y = int(input("Введите расходы: "))

if x > y:
    z = x - y
    print("Вы в плюсе на", z)
    p = int(input("Введите колличество сотрудников: "))
    zp = (z / p)
    print("Прибыль на одного сотрудника состовляет ", f"{zp:.2f}")
else:
    z = x - y
    print("Вы в минусе на: ", z)
    p = int(input("Введите колличество сотрудников: "))
    zp = (z / p)
    print("Убыток на одного сотрудника состовляет ", f"{zp:.2f}")

# 6 задание

a = int(input("Введите пройденное растояние: "))
b = int(input("Введите требуемый результат: "))
day = 0
while b - a >= 0:
    a = a + (a * 0.1)
    day += 1
print(day)
