#площадь квадрата
def square(a):
    from math import ceil
    return ceil(a ** 2)

a = float(input("Длина стороны квадрата: "))
result = square(a)
rounded_result = ceil(result)
print(f'Округленная в большую сторону сумма - {rounded_result}')