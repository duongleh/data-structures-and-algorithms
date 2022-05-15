# https://leetcode.com/problems/product-of-array-except-self
# O(N) TS


def product_of_array_except_self(nums: list[int]) -> list[int]:
    products = [1] * len(nums)
    prefix = postfix = 1

    for index, num in enumerate(nums):
        products[index] *= prefix
        prefix *= num

        products[-1 - index] *= postfix
        postfix *= nums[-1 - index]

    return products
