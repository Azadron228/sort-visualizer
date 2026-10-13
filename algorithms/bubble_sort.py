"""Пузырьковая сортировка с подсчётом сравнений."""


def bubble_sort(values):
    data = list(values)
    comparisons = 0
    for end in range(len(data) - 1, 0, -1):
        changed = False
        for index in range(end):
            comparisons += 1
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                changed = True
        # Отсортированный массив не требует следующих проходов.
        if not changed:
            break
    return data, comparisons
