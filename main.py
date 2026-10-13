"""Запуск: python main.py. Все настройки находятся в начале файла."""

from pathlib import Path
import random
import os
import sys

from algorithms import bubble_sort, quick_sort


SIZES = [20, 50, 100, 200, 400, 800]
SAMPLES = 8  # Число массивов каждого размера и типа.
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


def generate_array(size, kind, rng):
    if kind == "Много повторов":
        return [rng.randint(1, 5) for _ in range(size)]
    data = [rng.randint(1, max(1, size * 3)) for _ in range(size)]
    if kind != "Случайные":
        data.sort(reverse=kind == "Обратный порядок")
    if kind == "Почти отсортированные" and size > 1:
        for _ in range(max(1, size // 20)):
            left, right = rng.sample(range(size), 2)
            data[left], data[right] = data[right], data[left]
    return data


def measure_comparisons(rng):
    results = {name: [] for name in ALGORITHMS}
    for size in SIZES:
        totals = {name: 0 for name in ALGORITHMS}
        for _ in range(SAMPLES):
            values = generate_array(size, ARRAY_TYPE, rng)
            # Все алгоритмы получают одинаковые исходные данные.
            for name, sort in ALGORITHMS.items():
                _, comparisons = sort(values)
                totals[name] += comparisons
        for name in ALGORITHMS:
            results[name].append(totals[name] / SAMPLES)
    return results


def show_complexity(plt, results):
    _, ax = plt.subplots(figsize=(8, 5), layout="constrained")
    for name, comparisons in results.items():
        ax.plot(SIZES, comparisons, "o-", label=name)
    ax.set(title=f"Сложность алгоритмов · {ARRAY_TYPE}\nМеньше — лучше",
           xlabel="Размер массива", ylabel="Вычислительная сложность (среднее число сравнений)")
    ax.grid(True)
    ax.legend()


def main():
    if not ALGORITHMS:
        raise SystemExit("Добавьте хотя бы один алгоритм в ALGORITHMS в main.py")
    # Используем зависимости проекта даже без ручной активации окружения.
    environment = Path(__file__).resolve().parent / ".venv"
    interpreter = environment / "bin" / "python"
    if interpreter.exists() and Path(sys.prefix).resolve() != environment.resolve():
        os.execv(str(interpreter), [str(interpreter), str(Path(__file__).resolve())])

    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as error:
        raise SystemExit("Не установлен matplotlib. Установите зависимости в .venv "
                         "по инструкции в README.md") from error

    plt.rcParams["font.family"] = "DejaVu Sans"  # Поддержка кириллицы.
    results = measure_comparisons(random.Random(SEED))
    show_complexity(plt, results)
    plt.show()


if __name__ == "__main__":
    main()

