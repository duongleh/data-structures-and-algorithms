# https://www.lintcode.com/problem/paint-fence
# O(N) T | O(1) S


def num_ways_of_paint_fence(n: int, k: int) -> int:
    same, diff = 0, k
    for _ in range(1, n):
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff
