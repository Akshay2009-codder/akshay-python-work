class Linkedlist:
  def __init__(self):
    self.head = None

  def bigining(self,data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

l1 = Linkedlist()
l1.bigining(10)