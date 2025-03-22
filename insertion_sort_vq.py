from time import sleep
def insertion_sort(data):
  # Sort the given Array with insertion sort method
  #(Ascending order)
  for index in range(1,len(data)):
    temp = data[index]
    position=index
    while position>0 and data[position-1]>temp: # shifting
      data[position]=data[position-1] # copy right
      position=position-1
    data[position]=temp         # inseting
    print(data)
    sleep(1)
  return data
numbers = [91,23,45,72,12,1,6]
print(insertion_sort(numbers))
