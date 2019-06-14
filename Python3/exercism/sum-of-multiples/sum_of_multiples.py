def sum_of_multiples(limit, multiples):
    candidates = {element
                  for multiple in multiples if multiple
                  for element in range(multiple, limit, multiple)}
    return sum(candidates)
