def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid_el = arr[len(arr) // 2]
    left = [x for x in arr if x < mid_el]
    middle = [x for x in arr if x == mid_el]
    right = [x for x in arr if x > mid_el]
    return quick_sort(left) + middle + quick_sort(right)
print(quick_sort([1, 3, 5, 2, 15, 4]))