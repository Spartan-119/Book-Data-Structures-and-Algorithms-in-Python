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