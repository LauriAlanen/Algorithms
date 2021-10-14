sorted_list = [5, 6, 12, 30, 50, 60, 70, 100, 200, 355, 400]
target = 100


def binary_search(list_1, n):

    lower = 0
    upper = len(list_1) - 1

    if list_1[0] == n:
        return 0

    while lower <= upper:
        mid_val = (lower + upper) // 2

        if list_1[mid_val] == n:
            return mid_val

        else:
            if list_1[mid_val] < n:
                lower = mid_val + 1
            else:
                upper = mid_val - 1
    return -1


result = binary_search(sorted_list, target)

if result == -1:
    print(f"Value {target} is not in the ist!")

else:
    print(f"Value {target} found at index {result}")
