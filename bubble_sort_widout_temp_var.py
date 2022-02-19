def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if (list1[j]>list1[j+1]):

                #here we are not using temp var


                list1[j],list1[j+1]=list1[j+1],list1[j]

    return list1

list1=[24,75,44,72,9]

print("The unsorted list is : ",list1)

    #calling bubble sort
print("The sorted list is : ",bubble_sort(list1))