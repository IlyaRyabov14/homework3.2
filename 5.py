list = list(map(float, input("Введите числа через пробел:\n").split()))
new_list = [round(i % 1, 2) for i in list if i % 1 != 0]
print(max(new_list) - min(new_list))