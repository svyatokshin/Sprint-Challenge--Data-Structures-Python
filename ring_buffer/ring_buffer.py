from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # set an oldest value to use later if we go over capacity and need to remove an item
        self.oldest = None
        # calls the doublylinkedlist class so that we have a head and tail for our storage
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:  # checking to see if the list is at capacity
            # if it is not at capacity we just add new item to tail
            self.oldest = self.storage.head
            self.storage.add_to_tail(item)

        else:
            self.oldest.value = item  # setting current value to the node

            if self.oldest is not self.storage.tail:  # if its not the tail we are moving to tthe next one
                self.oldest = self.oldest.next
            else:
                self.oldest = self.storage.head

    def get(self):
        content_list = []          # creating an empty list then looping through the nodes
        node = self.storage.head    # while loop travering through the list

        while node is not None:     # adding value to the list once loop is done
            content_list.append(node.value)
            node = node.next        # moving to the next value
        return content_list        # returning the list


# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']
