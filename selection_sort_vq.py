from time import sleep
def selection_sort(data):
  # Sort the given Array with selection sort method
  #(Ascending order)
  for index in range(len(data)):
    small_index = index
    for i in range(index+1,len(data)): # finding smallest
      if (data[i]<data[small_index]):
        small_index=i
        print(data)
        sleep(1)

    # This if statement is only a very small improvement to the script
    # Does not make much impact
    if index != small_index:
      temp=data[index] # swapping only if required
      data[index]=data[small_index]
      data[small_index]=temp
      print(data)
      sleep(1)

  return data

numbers = [91,23,45,72,12,1,6]
print(selection_sort(numbers))
