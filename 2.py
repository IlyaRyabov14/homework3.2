list1 = [1,2,3,4,5,6,7,8]
list2 = []
count = len(list1)
for i in list1:
    if(count!=i):
        list2.append(list1[i-1] * list1[count-i])
    

print(list1," ==> ",list2)
