def jump_search(array, target):
  """Searches for an element in a sorted array using jump search.

  Args:
    array: A sorted array.
    target: The element to search for.

  Returns:
    The index of the target element in the array, or -1 if the element is not found.
  """

  # Set the jump step size.
  step = int((len(array))**0.5)

  # Initialize the start and end indices of the current block.
  start = 0
  end = step

  # Search for the target element in the current block.
  while start < len(array) and array[end] <= target:
    if array[end] == target:
      return end
    start += step
    end += step

  # If the target element is not found in the current block, perform a linear
  # search from the start of the block to the end of the array.
  for i in range(start, end):
    if array[i] == target:
      return i

  # If the target element is not found in the array, return -1.
  return -1


# Example usage:

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
target = 19

index = jump_search(array, target)

if index != -1:
  print(f"The target element {target} is found at index {index}.")
else:
  print(f"The target element {target} is not found in the array.")
