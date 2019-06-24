def recursiveSearch(array, value, indexFrom, indexTo):

  if indexTo-indexFrom == 1:
    if array[indexFrom] == value:
        return indexFrom
    else:
        return -1;

  slice = int((indexTo - indexFrom) / 2)

  if array[indexFrom + slice] > value:
    return recursiveSearch(array, value, indexFrom, indexTo - slice)
  else:
    return recursiveSearch(array, value, indexFrom + slice, indexTo)

def binarysearch(array, value):
  return recursiveSearch(array, value, 0, len(array))

array = [0, 1, 30, 31, 45, 46, 100, 120]

print('Find position of 31 in [%s]' % ', '.join(map(str, array)))
print(str(binarysearch(array, 31)))