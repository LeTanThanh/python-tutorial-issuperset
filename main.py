if __name__ == "__main__":
  # Python issuperset() method examples

  numbers = {1, 2, 3, 4, 5}
  scores = {1, 2, 3}

  print(numbers)
  print(scores)
  print(numbers.issuperset(scores))
  print(numbers.issuperset(numbers))
  print(scores.issuperset(numbers))

  # Using superset operators

  """
  set_a >= set_b
  """

  numbers = {1, 2, 3, 4, 5}
  scores = {1, 2, 3}

  print(numbers)
  print(scores)
  print(numbers >= scores)
  print(numbers >= numbers)
  print(scores >= numbers)

  print(numbers > scores)
  print(numbers > numbers)
  print(scores > numbers)
