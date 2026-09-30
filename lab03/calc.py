def c(a, b, o):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
a = float(input("Введите первое число: "))
o = input("Введите знак: ")
b = float(input("Введите второе число: "))
print("Результат: ", c(a, b, o))

