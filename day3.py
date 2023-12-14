#1.DELETION FROM SLL
def remove(self, index):
    if index < 0 or index >= self.length:
        return None

    # if node to be removed is the head node
    elif index == 0:
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    else:
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        popped_node = temp.next

        # if node to be removed is the tail node
        if popped_node.next is None:
            self.tail = temp

        temp.next = temp.next.next
        popped_node.next = None
        self.length -= 1
        return popped_node

#REVERSE A SLL
def reverse(self):
    prev_node = None
    current_node = self.head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    self.head, self.tail = self.tail, self.head


#Middle of SLL
def find_middle(self):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


#REMOVE DUPLICATES FROM UNSORTED LL


