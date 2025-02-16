# O(1) - Константное время
# Алгоритм работает за фиксированное время

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_element_by_index(lst, index):
    return lst[index]

print(get_element_by_index(lst=lst, index=4))

# O(log n) - Логарифмическое время
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid -1

    return -1

print(binary_search(lst,9))


# def binary_search(lst, target):
#     left, right = 0, len(lst) - 1
#
#
# while left <= right:
#     mid = (left + right) // 2
#     if lst[mid] == target:
#         return mid
#     elif lst[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
#
# return -1
#
# print(binary_search(lst, 9))





# O(n^2) - Квадратичное время

lst3 = [1,12, 2, 53, 84, 5, 76, 27, 18, 9]

def bubble_sort(lst):
    n = len(lst)
    print("for 1 --", range(n))
    for i in range(n):
        print(i)
        print("for 2--", range(n -i - 1))
        for j in range(n - i - 1):
            print("for 3--", j)
            if lst[j] > lst[j + 1]:
                print(f"{lst[j]}---{lst[j + 1]}, {lst3}")
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

bubble_sort(lst=lst3)
print(lst3)