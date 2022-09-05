def binary_search(data, target, low, high):
    if low > high:
        return "The element is NOT present in the list."
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            result = "The element is present at the index: " + str(mid)
            return result
        elif target < data[mid]:
            # recur on the left portion of mid
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

data = [1, 2, 5, 10, 40, 41]
print(binary_search(data, 10, 0, 6))