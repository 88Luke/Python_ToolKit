def merge(left,right):
  result=[]
  i,j=0,0
  while i<len(left) and j<len(right):
    if left[i]<=right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1
  result += left[i:]
  result += right[j:]
  return result


def merge_sort(data):
  # Sort myself using a merge sort.
  if len(data) <=1:
    return data
  middle = len(data)//2
  left=merge_sort(data[:middle])
  right=merge_sort(data[middle:])
  return merge(left,right)

numbers = [91,23,45,72,12,1,6]
print(merge_sort(numbers))
