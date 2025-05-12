from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def remove_two_elements(stones, index_x, index_y):
            max_index = max(index_x, index_y)
            min_index = min(index_x, index_y)
            stones.pop(max_index)
            stones.pop(min_index)

        while len(stones) > 1:
            biggest = second_biggest = 0
            index_x = index_y = None
            for i, v in enumerate(stones):
                if v >= biggest:
                    second_biggest, index_y = biggest, index_x
                    biggest, index_x = v, i
                elif v >= second_biggest:
                    second_biggest, index_y = v, i

            if biggest == second_biggest:
                remove_two_elements(stones, index_x, index_y)
            else:
                remove_two_elements(stones, index_x, index_y)
                stones.append(biggest - second_biggest)

        return stones[0] if stones else 0
