# O(1) - константная сложность
#✅Константная сложность означает, что время выполнения алгоритма не зависит от размера входных данных.

def getElement(arr, index):
    return arr[index]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(getElement(arr, 4))

# O(n) - линейная сложность алгоритма
#Линейная сложность алгоритма означает, что время выполнения алгоритма пропорционально количеству входных данных.
def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print(line_search(arr, 30))
print(line_search(arr, 60))

# O(log n) = логарифмическая сложность алгоритма
def binary_search(arr, target):
    low, high = 0, len(arr)- 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binary_search(arr, 70))  # выведет 6
print(binary_search(arr, 25))  # выведет -1