class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # Check if there's currently still space on the ring buffer
        if self.current < self.capacity:
            # Insert item at the current index in the storage
            self.storage[self.current] = item
            # Increment the the current count by 1
            self.current += 1

        # If storage is full
        if self.current == self.capacity:
            # reset the current to start overwriting from the first item
            self.current = 0

    def get(self):
        # Print items in the storage if item is not None
        return [print(item) for item in self.storage if item is not None]

###
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
