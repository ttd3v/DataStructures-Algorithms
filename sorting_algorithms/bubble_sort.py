def bubble_sort(sortingList):
    for i in range(len(sortingList)):
        for index in range(len(sortingList)):
            if index + 1 < len(sortingList) and sortingList[index] > sortingList[index + 1]:
                box = sortingList[index + 1]
                sortingList[index + 1] = sortingList[index]
                sortingList[index] = box
                del box
    return sortingList


to_sort = [1000 - x for x in range(1000)]
bubble_sort(to_sort)
print(to_sort)
