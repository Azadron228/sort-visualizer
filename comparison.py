"""Сравнение алгоритмов по числу сравнений и времени в миллисекундах."""

import random
from time import perf_counter

import matplotlib.pyplot as plt


from algorithms import bubble_sort, shaker_sort, insertion_sort


SIZES = list(range(100, 1001, 100))  # 10 размеров с равномерным шагом.
SAMPLES = 8  # Сколько массивов проверять для каждого размера.
SEED = 42
ARRAY_TYPE = "Случайные"

# Здесь выбирайте алгоритмы: добавляйте или удаляйте строки.
# Каждый алгоритм импортируется выше из своего файла.
ALGORITHMS = {
    "Пузырьковая (обменная) сортировка — O(n²)": bubble_sort,
    "Шейкерная сортировка — O(n²)": shaker_sort,
    "Сортировка включением — O(n²)": insertion_sort,
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


def measure_algorithms():
    """Возвращает среднее число сравнений и время сортировки в мс."""
    random_generator = random.Random(SEED)
    results = {name: [] for name in ALGORITHMS}
    times = {name: [] for name in ALGORITHMS}

    for size in SIZES:
        totals = {name: 0 for name in ALGORITHMS}
        total_times = {name: 0.0 for name in ALGORITHMS}

        for _ in range(SAMPLES):
            values = generate_array(size, ARRAY_TYPE, random_generator)

            # Каждый алгоритм получает один и тот же исходный массив.
            for name, sort in ALGORITHMS.items():
                started = perf_counter()
                _, comparisons = sort(values)
                elapsed_ms = (perf_counter() - started) * 1000
                totals[name] += comparisons
                total_times[name] += elapsed_ms

        for name in ALGORITHMS:
            results[name].append(totals[name] / SAMPLES)
            times[name].append(total_times[name] / SAMPLES)

    return results, times


def show_results(results, times):
    """Строит графики числа сравнений и времени в одном окне."""
    figure, (comparison_axis, time_axis) = plt.subplots(
        1, 2, figsize=(14, 6), layout="constrained"
    )
    figure.suptitle(f"Сравнение сортировок · {ARRAY_TYPE}\nМеньше — лучше")
    for name in ALGORITHMS:
        comparison_axis.plot(SIZES, results[name], "o-", label=name)
        time_axis.plot(SIZES, times[name], "o-", label=name)
    comparison_axis.set(title="Число сравнений", ylabel="Среднее число сравнений")
    time_axis.set(title="Время сортировки", ylabel="Среднее время, мс")
    for axis in (comparison_axis, time_axis):
        axis.set_xlabel("Размер массива")
        axis.set_ylim(bottom=0)
        axis.grid(True)
        axis.legend()


def main():
    plt.rcParams["font.family"] = "DejaVu Sans"  # Поддержка кириллицы.
    results, times = measure_algorithms()
    show_results(results, times)
    plt.show()


if __name__ == "__main__":
    main()
