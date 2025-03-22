from time import sleep
def bubbleSortTrackingExchange(data) :
# Sort the given Array with Bubble sort method (Ascending order)
# We keep track if exchanges were made and
# stop if no exchanges are made in a given pass
  exchange = True
  last = len(data)-1
  while exchange and last>0:
    exchange = False
    for current in range (last):
      if ( data[current] > data[current+1] ):
        temp = data[current]
        data[current]=data[current+1]
        data[current+1]=temp
        exchange = True
        print(data)
        sleep(1)
    last-=1
  return data
numbers = [91,23,45,72,12,1,6]
print(bubbleSortTrackingExchange(numbers))
