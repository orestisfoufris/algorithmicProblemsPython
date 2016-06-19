
"""
count inversions on an array
"""

count = 0


def merge_sort(array):
    if len(array) == 1 or len(array) < 1:  # base case
        return array, 0

    int_mid = len(array) / 2

    left, l = merge_sort(array[:int_mid])
    right, r = merge_sort(array[int_mid:])

    return merge_arrays(left, right, int_mid)


def merge_arrays(left, right, mid):
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
            global count
            count += mid - left_index

        if right_index >= len(right):
            for i in range(left_index, len(left)):
                new_array.append(left[i])
            break
        elif left_index >= len(left):
            for i in range(right_index, len(right)):
                new_array.append(right[i])
            break

    return new_array, count


if __name__ == '__main__':
    arr = []
    with open("IntegerArray.txt") as f:
        for line in f:
            arr.append(int(line))
    a, c = merge_sort(arr)
    print c
