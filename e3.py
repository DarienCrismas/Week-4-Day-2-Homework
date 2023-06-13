"""
Exercise #3

Use binary search to return the index of the target num
"""

cool_list = [2, 5, 6, 12, 45, 47, 98, 123, 1000]
target = 123

def e3(array, targetted, left, right):
    while left <= right:
        mid = (left + right) // 2
        check = array[mid]
        if targetted == check:
            return f"Index of {targetted} in {array}: {mid}"
        elif targetted < check:
            right = mid - 1
        else:
            left = mid + 1

print(e3(cool_list, target, 0, len(cool_list) -1))