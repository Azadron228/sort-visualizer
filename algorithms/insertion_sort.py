def insertion_sort(values, on_step=None):
    """Включает очередной элемент в отсортированную часть соседними обменами."""
    arr = values.copy()
    comparisons = 0

    for i in range(1, len(arr)):
        j = i
        while j > 0:
            comparisons += 1
            ordered = arr[j - 1] <= arr[j]
            if not ordered:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            if on_step:
                on_step(arr.copy(), (j - 1, j))
            if ordered:
                break
            j -= 1

    return arr, comparisons
