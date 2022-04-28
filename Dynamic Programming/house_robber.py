# https://leetcode.com/problems/house-robber
# O(N) T - O(1) S


def house_robber(houses: list[int]) -> int:
    second_last_house = last_house = 0
    for house in houses:
        second_last_house, last_house = last_house, max(second_last_house + house, last_house)

    return last_house
