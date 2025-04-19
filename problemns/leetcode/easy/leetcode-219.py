from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        for i, v in enumerate(nums):
            if v in hashmap:
                if abs(hashmap[v] - i) <= k:
                    return True
                else:
                    hashmap[v] = i
            else:
                hashmap[v] = i
        return False
