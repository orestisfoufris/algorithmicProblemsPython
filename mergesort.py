"""
merge sort algorithm in python
"""


def merge_sort(array):
    if len(array) == 1 or len(array) < 1:  # base case
        return array

    int_mid = len(array) / 2

    left = merge_sort(array[:int_mid])
    right = merge_sort(array[int_mid:])

    return merge_arrays(left, right)


def merge_arrays(left, right):
    left_index = 0
    right_index = 0
    new_array = []
    size = (len(left) + len(right))

    for i in range(size):
        if left[left_index] <= right[right_index]:
            new_array.append(left[left_index])
            left_index += 1
        else:
            new_array.append(right[right_index])
            right_index += 1

        if right_index >= len(right):
            for i in range(left_index, len(left)):
                new_array.append(left[i])
            break
        elif left_index >= len(left):
            for i in range(right_index, len(right)):
                new_array.append(right[i])
            break
    return new_array


if __name__ == '__main__':
    print merge_sort([8, 5, 3, 4, 6])
    print merge_sort([10, 9, 8, 7, 6, 5, 4])
    print merge_sort([1, 2, 3, 4, 5])
    print merge_sort(['b', 'c', 'a'])
    print merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    print merge_sort([])
