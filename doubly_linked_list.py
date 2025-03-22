class DLinkedListNode:
  
  def __init__(self, init_data, init_next, init_previous):

    self.data = init_data
    self.next = init_next
    self.previous = init_previous
    if (init_previous != None):
      init_previous.next = self
    if (init_next != None):
      init_next.previous = self

  def get_data(self):
    return self.data
  def get_next(self):
    return self.next
  def get_previous(self):
    return self.previous
  def set_data(self, new_data):
    self.data = new_data
  def set_next(self, new_next):
    self.next= new_next
  def set_previous(self, new_previous):
    self.previous= new_previous
  def __str__(self):
    return f"{self.data}"



class DLinkedList:
  def __init__(self):

    self.head = None
    self.tail = None
    self.size = 0

  def add(self, item):
    # adds an item to list at the beginning
    temp = DLinkedListNode(item, self.head, None)
    if self.head == None: # list is empty
      self.tail = temp
    self.head = temp
    self.size += 1

  def append(self, item):
    # adds the item to the end of the list
    # must traverse the list to the end and add item
    temp = DLinkedListNode(item, None, self.tail)
    if (self.head == None): # empty list?
      self.head=temp
    self.tail=temp
    self.size +=1

  def insert(self, pos, item):
    temp = DLinkedListNode(item, None, None)

        if pos == 0:
            temp.set_next(self.head)
            if self.head is not None:
                self.head.set_previous(temp)
            self.head = temp
            if self.tail is None:
                self.tail = temp
            self.size+=1
            return
        
        current = self.head
        for i in range(0, pos - 1):
            if current is None:
                print("Position is out of bounds.")
                return
            current = current.get_next()

  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.get_data() == item:
        found= True
      else:
        current = current.get_next() #.getPrevious()
    return found

  def index(self, item):
    current = self.head #self.tail
    found = False
    index = 0 #self.size-1
    while current != None and not found:
      if current.get_data() == item:
        found= True
      else:
        current = current.get_next() #getPrevious()
        index = index + 1 #index-1
    if not found:
      index = -1
    return index

  def remove(self, item):
    # search for the item and remove it
    # the method assumes the item exists
    current = self.head
    previous=None
    found = False
    while not found:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()
    if previous == None: # first node
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())# not the first node
    if (current.getNext() != None):# not the last node
      current.getNext().setPrevious(previous)
    else: # last node
      self.tail=previous
    self.size -= 1
