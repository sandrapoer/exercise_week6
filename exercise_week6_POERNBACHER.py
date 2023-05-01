# QUESTION NR 1
def power(a: int, b: int):
    if a <= 0 or b <= 0:
        return -1
    elif b == 1:
        return a
    else:
        return a ** b

# QUESTION NR 2
def binary_search(numbers, num):
    # get length of list
    n = len(numbers)

    # if list is emtpy, num is not in the list
    if n == 0:
        return -1

    # calculate middle of the list
    mid = n // 2

    # check if middle element is num
    if numbers[mid] == num:
        return mid

    # check if element is in the left half of the list
    elif numbers[mid] > num:
        # search on the left half of the list >> recursion
        return binary_search(numbers[:mid], num)

    # check if element is in the right half of the list
    else:
        # search on the right half of the list >> recursion
        result = binary_search(numbers[mid + 1:], num)
        if result != -1:
            return mid + 1 + result
        else:
            # if num not in the list
            return -1
