"""Быстрая сортировка с подсчётом сравнений."""


def quick_sort(values):
    data = list(values)
    comparisons = 0
    # Стек позволяет обойтись без рекурсии.
    stack = [(0, len(data) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = data[high]  # Последний элемент — опорный.
        boundary = low
        for index in range(low, high):
            comparisons += 1
            if data[index] <= pivot:
                data[index], data[boundary] = data[boundary], data[index]
                boundary += 1
        data[boundary], data[high] = data[high], data[boundary]
        stack.extend([(low, boundary - 1), (boundary + 1, high)])
    return data, comparisons

