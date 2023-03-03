lst = [14, 2.5, 34, 16, 183, 50, 1.16]

def bubble_sort(lst):
    length = len(lst)
    for i in range(length):
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

sorted_lst = bubble_sort(lst)
print(sorted_lst)


def binary_search(sorted_lst, item):
    start = 0
    end = len(sorted_lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if sorted_lst[mid] == item:
            return mid
        elif item < sorted_lst[mid]:
            end = mid - 1
        else:
            start = mid + 1

result = binary_search(lst, 14)
print(result)