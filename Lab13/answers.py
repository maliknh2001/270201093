def selectionSort(lst):
  if len(lst)== 1:
    return lst
  else:
    x1 = lst[0]
    x = 0
    for i in range(len(lst)):
      if x1>lst[i]:
        x1=lst[i]
        x = i
    lst[0], lst[x] = x1, lst[0]
    return [lst[0]] + selectionSort(lst[1:])


def binarySearch(lst, item):
  if len(lst) == 0:
    return -1
  else:
    mid_point = len(lst)//2
    smaller_list = lst[mid_point+1:] 
    larger_list = lst[:mid_point-1]
    if lst[mid_point] == item:
      return mid_point
    elif lst[mid_point] < item:
      return binarySearch(larger_list,item) 
    else:
      return binarySearch(smaller_list, item) 

print(binarySearch([1,2,3,4,5,6,7,8,9],5))