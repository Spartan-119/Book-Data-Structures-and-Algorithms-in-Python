import ctypes

class DynamicArray:
    def __init__(self) -> None:
        '''
        Create an empty arrary.
        '''
        self._n = 0             # count array elements
        self._capacity = 1      # setting the capacity of the new array
        self._A = self._make_array(self._capacity)          # low-level array
    
    def _make_array(self, c):   # non public utility
        '''
        return new array with capacity c.
        '''
        return (c * ctypes.py_object)()

    def __len__(self) -> int:
        '''
        return number of elements stored in the array.
        '''
        return self._n
    
    def __getitem__(self, k):
        '''
        Returns an element at the index k.
        '''
        if not 0 <= k <= self._n:
            raise IndexError('Invalid index!')
        return self._A[k]

    def _resize(self, c) -> None:              # private utility
        '''
        Resizing the internal size to capacity c.
        '''
        B = self._make_array(c)                 # new bigger array with capacity c.
        for element in range(self._n):          # for each existing element in the previous array.
            B[element] = self._A[element]       # assign the elements in the corresponding index of the new array.
        self._A = B                             # assigning the pointers, meaning, use the bigger array from now on.
        self._capacity = c                      # update the capacity.

    
    def append(self, obj) -> None:
        '''
        Add object at the end of the array.
        '''
        if self._n == self._capacity:           # not enough room
            self._resize(2 * self._capacity)    # so double the capacity
        self._A[self._n] = obj                  # add the obj at the end of the array
        self._n += 1                            # increase the length of the array