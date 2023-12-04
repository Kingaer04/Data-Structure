def selection_sort(array):
    length = len(array)
    for i in range(length):
        min_number = i
        print(min_number)
        for j in range(i+1, length):
            if array[j] < array[min_number]:
                min_number = j
                array[i], array[min_number] = array[min_number], array[i]
    return array


number = [0, 2, 5, 1, 7, -1, -100, 5, 7, 89, -1205]
print(selection_sort(number))
