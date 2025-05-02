from typing import List


def trap(height: List[int]) -> int:
    count = 0
    left = 0
    while left < len(height) - 2:
        mid = left + 1
        right = left + 2

        tempsum = 0

        x = height[left]

        if height[mid] > height[left]:
            left += 1
            continue
        if height[mid] < height[left] and height[mid] <= height[right]:
            tempsum += height[mid]
            tempsumtemp = tempsum
            temp_right = right

            while temp_right < len(height) - 1 and height[temp_right] < height[left]:
                tempsumtemp += height[temp_right]
                temp_right += 1

            if height[temp_right] >= height[left]:
                tempsum = tempsumtemp
                right = temp_right

            if height[temp_right] > height[right]:
                tempsum = tempsumtemp
                right = temp_right

            dis = abs(left - right) - 1
            heightc = min(height[left], height[right])
            area = (dis * heightc) - tempsum
            count += area
            left = right
            continue
        tempsum += height[mid]
        while right < len(height) - 1 and height[right] <= height[mid]:
            tempsum += height[right]
            right += 1

        tempsumtemp = tempsum
        temp_right = right

        while temp_right < len(height) - 1 and height[temp_right] < height[left]:
            tempsumtemp += height[temp_right]
            temp_right += 1

        if height[temp_right] >= height[left]:
            tempsum = tempsumtemp
            right = temp_right

        if height[right] >= height[mid]:
            dis = abs(left - right) - 1
            heightc = min(height[left], height[right])
            area = (dis * heightc) - tempsum
            count += area
            left = right
        else:
            left += 1
    return count


print(trap([3, 9, 2, 2, 8, 8, 7, 3]))
