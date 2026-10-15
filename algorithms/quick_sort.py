
def quick_sort(values, on_step=None):
    comparisons = 0

    def sort(arr):
        nonlocal comparisons

        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        left = []
        middle = []
        right = []

        for x in arr:
            comparisons += 1

            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

            if on_step:
                on_step(left + middle + right, ())

        return sort(left) + middle + sort(right)

    result = sort(list(values))
    return result, comparisons
