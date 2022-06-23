from typing import List


def my_sol(nums: List[int]) -> List[int]:
    length = len(nums)
    product_list = []
    reversed_product_list = []

    n = 1
    m = 1
    for i in range(length):
        n *= nums[i]
        m *= nums[length - i - 1]
        product_list.append(n)
        reversed_product_list.append(m)

    product_list = [1, *product_list[: length - 1]]
    reversed_product_list = [*reversed_product_list[length - 2 :: -1], 1]

    return [product_list[i] * reversed_product_list[i] for i in range(length)]


def sol1(nums: List[int]) -> List[int]:
    out = []
    p = 1

    for i in range(0, len(nums)):
        out.append(p)
        p *= nums[i]
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] *= p
        p *= nums[i]
    return out
