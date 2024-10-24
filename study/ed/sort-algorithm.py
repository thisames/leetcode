def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = key

    return list


print(insertion_sort([12, 11, 13, 5, 6]))
print(insertion_sort([12, 12, 13, 5, 6]))
