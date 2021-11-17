from unittest import TestCase
import pytest


def twoSum(nums, target):

    remainder = None

    for i in range(len(nums)):

        if remainder is None:

            if target - nums[i] in set(nums[i+1:]):

                remainder = target - nums[i]

                print(remainder, nums[i:])

                j = i

        elif remainder is not None and remainder == nums[i]:

            return [j, i]


# using hash maps

def twoSum(nums, target: int):

    diff_dict = {}

    for i, n in enumerate(nums):

        diff = target-n

        if diff in diff_dict:
            return diff_dict[diff], i

        diff_dict[n] = i


print(twoSum([3, 2, 4], 6))
