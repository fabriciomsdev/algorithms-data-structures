array = [1, 2, 6, 7, 8, 9, 10, 3, 4, 5]

def quicksort(array):
    less, greater, equal = [], [], []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array
    
print(quicksort(array))