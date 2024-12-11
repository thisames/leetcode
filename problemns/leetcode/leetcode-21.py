def mergeTwoLists(list1, list2):
    for i in range(len(list2)):
        for j in range(len(list1)):
            if list2[i] <= list1[j]:
                list1.insert(j, list2[i])
                break

    return list1


print(mergeTwoLists([2, 2, 4, 5], [1, 3, 4]))
