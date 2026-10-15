"""Анимация сортировки. Запуск: python animation.py."""

import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from algorithms import bubble_sort, quick_sort


ALGORITHM = "Пузырьковая"  # Варианты: Пузырьковая, Быстрая.
SIZE = 30
SEED = 42
INTERVAL = 60  # Задержка между кадрами в миллисекундах.

NORMAL_COLOR = "#4c78a8"
ACTIVE_COLOR = "#e15759"
DONE_COLOR = "#59a14f"


ALGORITHMS = {
    "Пузырьковая": bubble_sort,
    "Быстрая": quick_sort,
}


def create_frames(sort, values):
    """Запускает алгоритм и собирает его состояния для анимации."""
    frames = []

    def add_frame(data, active_indexes):
        frames.append((data, active_indexes, False))

    sorted_values, _ = sort(values, on_step=add_frame)
    frames.append((sorted_values, (), True))
    return frames


def main():
    if ALGORITHM not in ALGORITHMS:
        raise SystemExit(f"Неизвестный алгоритм: {ALGORITHM}")

    # Создаём перемешанный массив от 1 до SIZE.
    values = list(range(1, SIZE + 1))
    random.Random(SEED).shuffle(values)
    frames = create_frames(ALGORITHMS[ALGORITHM], values)

    figure, axis = plt.subplots(figsize=(9, 5), layout="constrained")
    bars = axis.bar(range(SIZE), values, color=NORMAL_COLOR)
    axis.set(
        title=f"{ALGORITHM} сортировка",
        xlabel="Позиция элемента",
        ylabel="Значение",
        xlim=(-0.8, SIZE - 0.2),
        ylim=(0, SIZE + 1),
    )

    def draw(frame):
        """Обновляет высоту и цвет столбиков для одного кадра."""
        data, active, done = frame
        active_indexes = set(active)

        for index, (bar, value) in enumerate(zip(bars, data)):
            bar.set_height(value)

            if done:
                bar.set_color(DONE_COLOR)
            elif index in active_indexes:
                bar.set_color(ACTIVE_COLOR)
            else:
                bar.set_color(NORMAL_COLOR)

        return bars

    # FuncAnimation вызывает draw для каждого сохранённого состояния.
    # Переменная animation хранит объект до закрытия окна.
    animation = FuncAnimation(
        figure,
        draw,
        frames=frames,
        interval=INTERVAL,
        repeat=False,
    )
    plt.show()


if __name__ == "__main__":
    main()
