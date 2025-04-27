from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        result = []

        while i < len(firstList):
            if i < len(firstList) and j < len(secondList) and (firstList[i][1] >= secondList[j][0] and secondList[j][1] >= firstList[i][0]):
                while i < len(firstList) and j < len(secondList) and (firstList[i][1] >= secondList[j][0] and secondList[j][1] >= firstList[i][0]):
                    a = max(secondList[j][0], firstList[i][0])
                    b = min(secondList[j][1], firstList[i][1])
                    intersections = [a, b]
                    result.append(intersections)
                    j += 1
            else:
                while i < len(firstList) and j < len(secondList) and not (firstList[i][1] >= secondList[j][0] and secondList[j][1] >= firstList[i][0]):
                    j += 1
                while i < len(firstList) and j < len(secondList) and (firstList[i][1] >= secondList[j][0] and secondList[j][1] >= firstList[i][0]):
                    a = max(secondList[j][0], firstList[i][0])
                    b = min(secondList[j][1], firstList[i][1])
                    intersections = [a, b]
                    result.append(intersections)
                    j += 1
            i += 1
            j = 0
        return result
