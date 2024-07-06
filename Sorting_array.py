# Bubble sort, selection sort , insertion sort

# Bubble Sort

sample_array = [2,4,6,7,5,4,1,2,3,99,77,66,55,75]
size = len(sample_array)
for i in range(size-1):
    for j in range(size-i-1):
        if sample_array[j] > sample_array[j+1]:
            sample_array[j], sample_array[j+1] = sample_array[j+1], sample_array[j]
print('SAmple bubble sort' ,sample_array)


# Efficient Bubble sort
bubble_array = [2,4,6,7,5,4,1,2,3,99,77,66,55,75]

length = len(bubble_array)
for i in range(length-1):
    swap = False
    for j in range(length-i-1):
       if bubble_array[j] >  bubble_array[j+1]:
           bubble_array[j],bubble_array[j+1] = bubble_array[j+1], bubble_array[j]
           swap = True

    if not swap:
       break 

print('Bubble Sort', bubble_array)

#Selection Sort
array_selection = [2,4,6,7,5,4,1,2,3,99,77,66,55,75]
L =len(array_selection)
for i in range(L-1):
    min_index = i
    for j in range(i+1, L):
        if array_selection[j] < array_selection[min_index]:
            min_index = j
    min_value = array_selection.pop(min_index)
    array_selection.insert(i, min_value)

print('Selection ',array_selection)

#Efficient Selection sort
array_selection2 = [2,4,6,7,5,4,1,2,3,99,77,66,55,75]
length = len(array_selection2)
for i in range(length):
    min_index = i
    for j in range(i+1, length):
        if array_selection2[j] < array_selection2[min_index]:
            min_index = j
    array_selection2[i], array_selection2[min_index] = array_selection2[min_index], array_selection2[i]

print(array_selection2)


#Insertion Sort

array_insertion = [2,4,6,7,5,4,1,2,3,99,77,66,55,75]

length = len(array_insertion)
for i in range(1, length):
    insert_index = i
    current_value = array_insertion[i]
    for j in range(i-1, -1, -1):
        if array_insertion[j] > current_value:
            array_insertion[j+1] = array_insertion[j]
            insert_index = j
        else:
            break
    array_insertion[insert_index] = current_value

print('Insertion sort', array_insertion)



