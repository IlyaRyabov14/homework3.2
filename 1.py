list1 = [1,2,3,4,5,6,7,8]
list2 = []
result = 0
for i in list1:
    if (i % 2 != 0):
        result += list1[i]
        list2.append(list1[i])

print(list1, "-->  на нечётных позициях элементы",list2,"ответ", result)