#Creating a bubble sort function

def bubble_sort(list1):

#outer loop to traverse aentire list

        for i in range(0,len(list1)-1):
            for j in range(len(list1)-1):
                if (list1[j]>list1[j+1]):
                    temp=list1[j]
                    list1[j]=list1[j+1]
                    list1[j+1]=temp
        return list1

list1=[4,9,0,3,8]

print("The unsorted list is: ",list1)

#calling bubble sort function

print("The sorted list is : ",bubble_sort(list1))
