def bubble_sort(values, on_step=None):
    arr = values.copy()
    comparisons = 0
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            if on_step:
                on_step(arr.copy(), (j, j + 1))

    return arr, comparisons

