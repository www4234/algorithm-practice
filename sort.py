def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Исходный массив: {test_data}")
    
    # Тест сортировки пузырьком
    bubble_res = bubble_sort(test_data.copy())
    print(f"Сортировка пузырьком: {bubble_res}")
    
    # Тест быстрой сортировки
    quick_res = quick_sort(test_data.copy())
    print(f"Быстрая сортировка: {quick_res}")
