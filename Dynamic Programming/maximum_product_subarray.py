# https://leetcode.com/problems/maximum-product-subarray
# O(N) T | O(1) S


def maximum_product_subarray(nums: list[int]) -> int:
    current_max_product = current_min_product = max_product = nums[0]

    for num in nums[1:]:
        products = (current_max_product * num, current_min_product * num, num)
        current_max_product, current_min_product = max(products), min(products)
        max_product = max(max_product, current_max_product)

    return max_product
