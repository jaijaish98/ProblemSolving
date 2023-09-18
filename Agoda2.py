def maximize_operator2(t, x, y):
  """
  Maximizes the number of times operator2 is used to get to number t.

  Args:
    t: the target number
    x: the value of operator1
    y: the value of operator2

  Returns:
    A list of strings where each string is of the form "operator_add n" or "operator_multiply n"
    where n is the number of times the operator is applied.
  """

  if t <= x:
    return ["no_solution"]

  # Initialize the queue with the initial state (1, 0).
  queue = [[1, 0]]

  # Iterate over the queue until we find a state where the current number is equal to t.
  while queue:
    current_number, current_operator_count = queue.pop(0)

    # If the current number is equal to t, then we have found a solution.
    if current_number == t:
      return ["operator_add" + str(current_operator_count)]

    # Add the state (current_number + x, current_operator_count + 1) to the queue.
    queue.append([current_number + x, current_operator_count + 1])

    # Add the state (current_number * y, current_operator_count) to the queue.
    queue.append([current_number * y, current_operator_count])

  return ["no_solution"]

# Read input

# Find and print the sequence of operations
operations = maximize_operator2(54, 1, 3)
print(operations)
