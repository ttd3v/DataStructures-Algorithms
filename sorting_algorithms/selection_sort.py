def selection_Sort(to_sort):
    unsorted = to_sort
    sorted = []
    for i in range(len(unsorted)):
        index = 0
        for idx in range(len(unsorted)):
            val = unsorted[idx]
            if val < unsorted[index]:
                index = idx
        value = unsorted.pop(index)
        sorted.append(value)
    return sorted

to_sort = selection_Sort([100000-x for x in range(100000)])
print(to_sort)
