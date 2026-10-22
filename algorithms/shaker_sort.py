def shaker_sort(values, on_step=None):
    """Сортирует соседними обменами, чередуя направления прохода."""
    arr = values.copy()
    comparisons = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        swapped = False
        for j in range(right, left, -1):
            comparisons += 1
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swapped = True
            if on_step:
                on_step(arr.copy(), (j - 1, j))

        if not swapped:
            break
        left += 1

        swapped = False
        for j in range(left, right):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            if on_step:
                on_step(arr.copy(), (j, j + 1))

        if not swapped:
            break
        right -= 1

    return arr, comparisons
