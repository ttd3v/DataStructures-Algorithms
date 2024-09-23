import random
def mergeSort(to_sort):
    if len(to_sort) <= 1:
        return to_sort
    length = len(to_sort)
    left = mergeSort(to_sort[:length//2])
    right = mergeSort(to_sort[length//2:])

    finish = []
    if len(left) > 0 and len(right) > 0 :
        for i in range(length):
            if len(left) == 0 or len(right) == 0:
                break
            if left[0] > right[0]:
                finish.append(right.pop(0))
                continue
            if right[0] > left[0]:
                finish.append(left.pop(0))
                continue
    else:
        if len(left) == 0:
            finish = right
        else:
            finish = left
    finish.extend(left)
    finish.extend(right)
    return finish
from time import time
import threading
lit = [500000-x for x in range(500000)]
print("List made")
started = time()
lit = mergeSort(lit)
print(time()-started)
#O(n log n)
