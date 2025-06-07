# The following operations must be the ones that a Queue must have
# Queue.enqueue() -> add element to start of the queue
# Queue.dequeue() -> remove element from the end of the queue 
#                    and raise an exception if the queue is empty
# Queue.first() -> return the first element from the queue
# Q.is_empty() -> return a True if the queue is empty or else False
# len(Q) -> return the number of elements in the queue


# Making a python list based stack

class Empty(Exception):
    '''Raise an empty exception if the queue is empty'''

class ArrayQueue():
    '''FIFO queue implementation using a python list as an underlying storage'''
    DEFAULT_CAPACITY = 10

    def __init__(self):
        '''Create an empty Queue'''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0 #actual elements
        self._front = 0
    
    def enqueue(self, e):
        '''Adds an element to the back of the queue'''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def dequeue(self):
        '''Removes an element from the end of the queue
        
        Raises Empty exception if teh queue is empty'''
        if self.is_empty():
            raise Empty("Cannot dequeue from an empty queue")
        
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def _resize(self, cap):
        '''Resize the queue by cap * previous size'''
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(len(old)):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0
    
    def first(self):
        '''Return a reference of the first element in the queue'''
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def is_empty(self):
        '''Return a boolean value based on if the queue is empty or not'''
        return self._size == 0
    
    def __len__(self):
        '''Return the actual number of elements in the queue'''
        return self._size
        
    def __repr__(self):
        """A better representation of the queue"""
        format = "in -> [ "
        for j in range(len(self._data)):
            format += str(self._data[j]) + ", "
        format += "] -> out"
        return format


if __name__ == "__main__":
    example = ArrayQueue()
    for number in range(1, 16):
        example.enqueue(number)
        print(f'Current queue: {example}. Current size of the queue: {example._size}. Current front: {example._front} \n')
        
    for numbers in range(1, 5):
        example.dequeue()
    
    print(f"Current queue after some deletions: {example}")
    
    for number in range(16, 28):
        example.enqueue(number)
        print(f'Current queue: {example}. Current size of the queue: {example._size}. Current front: {example._front} \n')


# [1,2,3,4,5] <- in -> append

# out <- [1,2,3,4,5] -> pop(0) -> inefficient 1st n-1 elments shift
# out <- [none, 2,3,4,5]
#               f -> next deque f=2
# [1,.....100] -> enque
# [] deque -> 50 elements -> [] -> shrink -> none

#length = n, actual elements after deque n/4 -> [] / 2