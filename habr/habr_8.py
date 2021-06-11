# Дан массив точек с целочисленными координатами (x, y).
# Определить, существует ли вертикальная прямая,
# делящая точки на 2 симметричных относительно этой прямой множества.
# Note: Для удобства точку можно представлять не как массив [x, y], а как объект {x, y}
from statistics import mean


def is_vertical_symmetry(points: List[Point]) -> bool:
    # сначала найдём вертикальную прямую в середине всех точек
    x_center = mean(p.x for p in points)

    # тут будем хранить точки, для которых пока не нашли пары:
    unmatched_points = defaultdict(int)

    for point in points:

        if point.x == x_center:  # если точка на прямой, то она сама себе пара
            continue

        # создадим "брата" - точку, которая симметрична текущей относительно вертикальной прямой
        brother = Point(
            x=x_center * 2 - point.x,
            y=point.y,
        )

        # если этот брат есть в unmatched_points, то достаём его оттуда и говорим, что текущая точка сматчилась
        if unmatched_points[brother]:
            unmatched_points[brother] -= 1

        # иначе добавляем эту точку в не-сматченные
        else:
            unmatched_points[point] += 1

    return not any(unmatched_points.values())
