import collections
from dis import dis
from typing import List


def my_sol(height: List[int]) -> int:
    # time exceeded
    volume = 0
    height_maps = collections.defaultdict(list)

    def fill(idx1, idx2, fill_height):
        idx = idx1 + 1
        filled_volume = 0
        while idx < idx2:
            if height[idx] < fill_height:
                for h in range(height[idx] + 1, fill_height + 1):
                    height_maps[h].append(idx)
                    height_maps[h].sort()
                    filled_volume += 1
                height[idx] = fill_height
            idx += 1
        return filled_volume

    for i, n in enumerate(height):
        for h in range(n + 1):
            height_maps[h].append(i)

    for h in sorted(height_maps.keys(), reverse=True):
        fill_index_list = [
            (height_maps[h][i], height_maps[h][i + 1])
            for i in range(len(height_maps[h]) - 1)
        ]
        for idx1, idx2 in fill_index_list:
            volume += fill(idx1, idx2, h)

    return volume


def sol1(height: List[int]) -> int:
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


def sol2(height: List[int]) -> int:
    stack = []
    volume = 0
    for i in range(len(height)):
        print(stack)
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume
