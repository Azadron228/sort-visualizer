"""Сравнение алгоритмов по среднему числу сравнений элементов."""

import random

import matplotlib.pyplot as plt


from algorithms import bubble_sort, quick_sort


SIZES = [20, 50, 100, 200, 400, 800]
SAMPLES = 8  # Сколько массивов проверять для каждого размера.
SEED = 42
ARRAY_TYPE = "Случайные"

# Здесь выбирайте алгоритмы: добавляйте или удаляйте строки.
# Каждый алгоритм импортируется выше из своего файла.
ALGORITHMS = {
    "Пузырьковая сортировка — O(n²)": bubble_sort,
    "Быстрая сортировка — O(n log n)": quick_sort,
}
# Варианты ARRAY_TYPE: Случайные, Отсортированные, Обратный порядок,
# Почти отсортированные, Много повторов.


def generate_array(size, array_type, random_generator):
    """Создаёт массив указанного размера и типа."""
    if array_type == "Много повторов":
        return [random_generator.randint(1, 5) for _ in range(size)]

    data = [random_generator.randint(1, size * 3) for _ in range(size)]

    if array_type == "Случайные":
        return data

    data.sort(reverse=array_type == "Обратный порядок")

    if array_type == "Почти отсортированные" and size > 1:
        for _ in range(max(1, size // 20)):
            left, right = random_generator.sample(range(size), 2)
            data[left], data[right] = data[right], data[left]

    return data


def measure_comparisons():
    """Запускает алгоритмы и возвращает среднее число сравнений."""
    random_generator = random.Random(SEED)
    results = {name: [] for name in ALGORITHMS}

    for size in SIZES:
        totals = {name: 0 for name in ALGORITHMS}

        for _ in range(SAMPLES):
            values = generate_array(size, ARRAY_TYPE, random_generator)

            # Каждый алгоритм получает один и тот же исходный массив.
            for name, sort in ALGORITHMS.items():
                _, comparisons = sort(values)
                totals[name] += comparisons

        for name in ALGORITHMS:
            results[name].append(totals[name] / SAMPLES)

    return results


def show_complexity(results):
    """Строит график по результатам измерений."""
    _, ax = plt.subplots(figsize=(8, 5), layout="constrained")

    for name, comparisons in results.items():
        ax.plot(SIZES, comparisons, "o-", label=name)

    ax.set(
        title=f"Сложность алгоритмов · {ARRAY_TYPE}\nМеньше — лучше",
        xlabel="Размер массива",
        ylabel="Среднее число сравнений",
    )
    ax.grid(True)
    ax.legend()


def main():
    plt.rcParams["font.family"] = "DejaVu Sans"  # Поддержка кириллицы.
    results = measure_comparisons()
    show_complexity(results)
    plt.show()


if __name__ == "__main__":
    main()
