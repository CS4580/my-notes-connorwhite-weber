"""Library to calculate number of digits
for different algorithms
"""
import math


def factorial_length(number):
  """Count the number of digits in a factorial number

  Args:
      number (int): integer value to calculate factorial

  Returns:
      int: number of digits for factorial of input
  """
  factorial = math.factorial(number)
  length = 0
  length = str(factorial)
  return len(length)


def main():
  """Driven Function, an entry point
  """
  number = 5
  digits = factorial_length(number)
  print(f'You have {digits} digit(s) in factorial({number})')

if __name__ == '__main__':
  main()