from typing import List


def search(self, nums: List[int], target: int) -> int:
    def binary_search(l, r):
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return - 1

    return binary_search(0, len(nums) - 1)