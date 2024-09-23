def inserction_sort(sortList):
    for i in range(len(sortList)):
        for index in range(len(sortList)):
                if index == 0:
                    continue
                value = sortList[index]
                for back_index in range(index,-1,-1):
                    if sortList[back_index] > value:
                        sortList[index] = sortList[back_index]
                        sortList[back_index] = value
                        break    
    return sortList
to_sort = [100-x for x in range(100)]
to_sort = inserction_sort(to_sort)
print(to_sort)
