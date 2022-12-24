
from enum import Enum

class OrderType(Enum):
    LESS = 'less'
    GREATER = 'greater'

execution_times = {
    'count': 0
}

def search_by(search_type: OrderType = OrderType.GREATER, array: list = []):
    current = array[0]
    current_index = 0
    for index in range(1, len(array)):
        if search_type == OrderType.GREATER and array[index] > current:
            current = array[index]
            current_index = index
        elif search_type == OrderType.LESS and array[index] < current:
            current = array[index]
            current_index = index
            
        execution_times['count'] += 1
    return current_index
    
    
def sort_by_selection(search_type: OrderType, array: list = []):
    new_array = []
    for _ in range(len(array)):
        index = search_by(search_type, array=array)
        new_array.append(array.pop(index))
    return new_array

array_to_sort = [500, 6, 7, 8, 9, 12, 60, 0]
sorted_array = sort_by_selection(OrderType.GREATER, array_to_sort.copy())

print('RESULT:')
print('-' * 25)
print('Before: \n', array_to_sort, '\n Length: ',len(array_to_sort))
print('After: \n', sorted_array, '\n Length: ',len(sorted_array))
print('Execution times: ', execution_times['count'])
print('-' * 25, '\n')
