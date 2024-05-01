if __name__ == "__main__":
  # Python issuperset() method examples

  numbers = {1, 2, 3, 4, 5}
  scores = {1, 2, 3}

  print(numbers)
  print(scores)
  print(numbers.issuperset(scores))
  print(numbers.issuperset(numbers))
  print(scores.issuperset(numbers))