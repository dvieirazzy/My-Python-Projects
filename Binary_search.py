def binary_search(num, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((right + left) / 2)
        if array[mid] == num:
            return mid
        else:
            if array[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
    return -1


list_of_lists_of_integers = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 1, 2, 6, 7, 8, 8, 9, 9, 9],
    [1, 2, 2, 3, 5, 6, 6, 7, 8, 9],
    [1, 2, 3, 3, 6, 7, 7, 8, 8, 9],
    [1, 1, 3, 4, 5, 7, 8, 8, 8, 10],
    [1, 1, 1, 2, 2, 3, 5, 7, 9, 9],
    [1, 1, 2, 2, 3, 5, 5, 10, 10, 10],
    [1, 1, 1, 1, 1, 3, 4, 5, 6, 7],
    [1, 1, 2, 3, 5, 5, 7, 7, 9, 10],
    [1, 1, 2, 2, 2, 4, 5, 6, 7, 9],
    [1, 1, 3, 5, 5, 7, 7, 8, 8, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
]

for i in list_of_lists_of_integers:
    i.sort()
    num5_index = binary_search(5, i)
    print(num5_index)
