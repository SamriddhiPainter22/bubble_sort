def bubble_sort(list1):

    #we can stop the iteration once swap has done

    has_swapped=True

    while(has_swapped):
        has_swapped=False


    for i in range(len(list1)-1):
        if (list1[i]>list1[i+1]):

            #swap


                list1[i],list1[i+1]=list1[i+1],list1[i]

    return list1

list1=[24,75,44,72,9]

print("The unsorted list is : ",list1)

    #calling bubble sort
print("The sorted list is : ",bubble_sort(list1))