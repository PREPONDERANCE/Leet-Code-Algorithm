#!/usr/bin/env python3


def containsDuplicate(nums: list[int]) -> bool:
    hashSet = set()
    for n in nums:
        if n in hashSet:
            return True
        hashSet.add(n)
    return False


# By creating a set, a container with no duplicate elements,
# we can add all the elements to the set while checking if there
# are duplicates in O(1) time.

# Overall Time Complexity : O(n)
# Overall Space Complexity: O(n)
